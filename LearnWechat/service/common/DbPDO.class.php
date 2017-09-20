<?php

/**
 * PDO操作类，创建数据库连接，执行具体业务的增、删、改、查操作
 * 待更新补充...
 */
class DbPDO {

    private static $_instance = null;		// 当前PDOx类的静态示例
    private $_conn;                 // 创建的PDO链接
    private static $_table;         // 要操作的数据表
    private $_fields				= '*';         // 要查询的字段
    private $_where					= '';           // where 设置
    private $_order					= '';           // order by 设置
	private $_limit				= '';

    /**
     * 初始化PDO链接，设置错误级别、字符集
     */
    private function __construct() {
        try {
            $this->_conn = new PDO(DB_DSN, DB_USER, DB_PWD);
        } catch(Exception $e) {
            die('Unable to connect to the database! Error: '.$e->getMessage());
        }
        $this->_conn->setAttribute(PDO::ATTR_EMULATE_PREPARES, false);
        $this->_conn->setAttribute(PDO::ATTR_ORACLE_NULLS, PDO::NULL_TO_STRING);
        $this->_conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        $this->_conn->exec("SET NAMES 'utf8'");
    }

    /**
     * 阻止克隆对象
     */
    private function __clone() { }

    /**
     * 获取当前类的实例，保证单例
     * @return object
     */
    private static function getInstance() {
        if(!self::$_instance) {
            self::$_instance = new self();
        }
        return self::$_instance;
    }

    /**
     * 以静态类方式调用方法时，自动执行次方法，如 PDOx::method();
     * @param  string $method    静态方法名
     * @param  array $arguments 参数数组
     * @return
     */
    final public static function __callStatic($method, $arguments) {
        $instance = self::getInstance();
        return call_user_func_array(array($instance, $method), $arguments);
    }

    /**
     * 非静态方式调用类中的方法，如 ->find()
     * @param  string $method    要调用的类方法
     * @param  array $arguments 调用方法时传的参数
     * @return
     */
    final public function __call($method, $arguments) {
        if (!method_exists(self::$_instance, $method)) {
            throw new Exception('Unknown method of ' . $method);
        }
        return call_user_func_array(array(self::$_instance, $method), $arguments);
    }

    /**
     * 设置要操作的数据表
     * @param  string $tbName 表名
     * @return object 当前类的实例
     */
    private static function table($tbName) {
        self::$_table = "`".DB_TB_PREFIX.strtolower($tbName)."`";
        return self::$_instance;
    }

    /**
     * 查询
     * @return
     */
    private function find() {
        $sql = "SELECT ".$this->_fields." FROM ".self::$_table.$this->_where.$this->_order.$this->_limit;
		//echo $sql;
		// exit;
        try {
            $stmt = $this->_conn->query($sql);
            $affectedRows = $stmt->rowCount();
            if($affectedRows > 0) {
                $stmt->setFetchMode(PDO::FETCH_ASSOC);
                return $stmt->fetchAll();
            } else { // 没有指定的记录
				//throw new Exception('No specified record!');
				return false;
            }
        } catch(Exception $e) {
			die('Error: ' . $e->getMessage());
        }
    }

    /**
     * 直接通过SQL遇见查询
     * @param  string $sql 要执行的SQL语句
     * @return array 执行结果
     */
    private function findBySQL($sql) {
        try {
            $stmt = $this->_conn->query($sql);
            $affectedRows = $stmt->rowCount();
            if($affectedRows > 0) {
                $stmt->setFetchMode(PDO::FETCH_ASSOC);
                return array('success'=>true, 'msg'=>'', 'data'=>$stmt->fetchAll());
            } else { // 没有指定的记录
                return array('success'=>false, 'msg'=>'No records!');
            }
        } catch(Exception $e) {
            return array('success'=>false, 'msg'=>'Select failed! Error: '.$e->getMessage());
        }
    }

    /**
     * 新增数据
     * @param array $data 要插入的数据，键值对形式
     * @return bool 是否执行成功
     */
    private function add($data) {

        $val = $this->_getFormattedData($data);
        $sql = "INSERT INTO ".self::$_table."(".$val['keys'].") VALUES(".$val['pos2'].")";

        try {
            $stmt = $this->_conn->prepare($sql);
            $affectedRows = $stmt->execute($val['values']);
            if($affectedRows > 0) {
                return true; // 插入成功
            }
        } catch (Exception $e) {
            echo json_encode(array('code'=>400, 'message'=>'Insert failed! Error: '.$e->getMessage()));
            exit;
        }
    }


    /**
     * 修改数据
     * @param  mixed $data 要修改的数据，可以是包含键和值的数组或sql语句片段
     * @return bool 是否执行成功
     */
    private  function save($data) {

        $val = $this->_getFormattedData($data);
        $sql = "UPDATE ".self::$_table." SET ".$val['k2v'].$this->_where;

        try {
            $affectedRows = $this->_conn->exec($sql);
            if($affectedRows > 0) {
                return array('success'=>true, 'msg'=>'');
            } else { // 没有指定的记录
                return array('success'=>false, 'msg'=>'No specified record or has changed!');
            }
        } catch(Exception $e) {
            return array('success'=>false, 'msg'=>'Update failed! Error: '.$e->getMessage());
        }
    }

    /**
     * 删除数据
     * 若调用此方法前没有调用$this->where()方法，则使用$this->_where的默认值“”，即删除表中所有数据
     * @return bool 是否执行成功
     */
    private function del() {

        $sql = "DELETE FROM ".self::$_table.$this->_where;

        try {
            $affectedRows = $this->_conn->exec($sql);
            if($affectedRows > 0) {
                return array('success'=>true, 'msg'=>'');
            } else { // 没有指定的记录
                return array('success'=>false, 'msg'=>'No specified record!');
            }
        } catch(Exception $e) {
            return array('success'=>false, 'msg'=>'Delete failed! Error: '.$e->getMessage());
        }
    }

    /**
     * 设置要查询的字段
     * @param  array $fieldArr 包含字段的数组
     * @return object $this
     */
    private function field($fields) {
		if(is_array($fields)) {

			$tmpFields = '';

			// 是否去重
			if(!empty($fields['distinct'])) {
				$tmpFields .= ' DISTINCT ';
				unset($fields['distinct']);
			}

			// 组合字段
			foreach($fields as $k => $v) {
                $tmpFields .= gettype($k) == 'string' ? "`{$k}` AS `{$v}`," : "`{$v}`,";
			}

			$this->_fields = substr($tmpFields, 0, -1);
		} else if(is_string($fields)) {
			$this->_fields = $fields;
		} else {
			throw new Exception('Unsuported paremeter type \'' . gettype($fields) . '\'');
		}

        return $this;
    }

    /**
     * 设置where的参数
     * @param  array $data 要处理的where条件数据
     * @return object 当前类对象
     */
    private function where($condition) {

		$this->_where = " WHERE ";

		if(is_array($condition)) {
			$val = $this->_getFormattedData($condition);
			$this->_where .= $val['k2v'];
		} else if(is_string($condition)) {
			$this->_where .= $condition;
		} else {
			throw new Exception('Unsuported paremeter type \'' . gettype($condition) . '\'');
		}

		return $this;
    }

    /**
     * 设置排序规则，如array('catId'=>"desc",'catName')
	 * 方式一：->order('`col2` DESC');
	 * 方式二：->order(array('desc'=>'col2'));
	 * @param  array $data 要处理的order规则数据
     * @return object 当前类对象
     */
    private function order($orders) {
		if(is_array($orders)) {
			$tmpOrders = '';
			foreach($orders as $k => $v) {
				if(gettype($k) == 'string') {
					$tmpOrders .= "`{$v}` " . strtoupper($k) . ",";
				} else {
					$tmpOrders .= "`{$v}`,";
				}
			}
			$this->_order = " ORDER BY " . substr($tmpOrders, 0, -1);
		} else {
			$this->_order = " ORDER BY " . $orders;
		}

        return $this;
    }

	/**
	 *
	 */
	private function limit($length, $offset=0) {
		$this->_limit =  " LIMIT {$offset},{$length}";
		return $this;
	}

   /**
     * 将待操作的数据格式化成不同格式，以便后面的操作
     * @param  array $data 要处理的数据
     * @return array
     */
    private function _getFormattedData($data) {

            $tmpArr = array();

            // 键个数
            $tmpArr['keyNum'] = count(array_keys($data));

            // 所有要操作的字段
            $tmpArr['keys'] = "`".join("`,`", array_keys($data))."`";

            // 包含所有字段对应值的数组
            $tmpArr['values'] = array_values($data);

            // 字段1=值1,字段2=值2 适用于 SET
            $tmpArr['k2v'] = "";
            foreach($data as $k => $v) {
                $vv = gettype($v) == 'string' ? "'".$v."'" : $v;
                $kk = "`".$k."`";
                $tmpArr['k2v'] .= $kk.'='.$vv.',';
            }
            $tmpArr['k2v'] = substr($tmpArr['k2v'], 0, -1);

            // 字段1=?, 字段2=?
            $tmpArr['k2pos2'] = '';
            foreach($data as $k => $v) {
                 $tmpArr['k2pos2'] .= "`".$k."` = ?,";
            }
            $tmpArr['k2pos2'] = substr( $tmpArr['k2pos2'], 0, -1);

            // 命名参数占位符 :name, :pwd
            $tmpArr['pos1'] = ':'.join(',:', array_keys($data));

            // ？号占位符
            $tmpArr['pos2'] = '';
            for($i = 0; $i < count($data); $i++) {
                $tmpArr['pos2'] .= '?,';
            }
            $tmpArr['pos2'] = substr($tmpArr['pos2'], 0, -1);

            return $tmpArr;
    }

    /**
     * 自动关闭PDO数据库连接
     */
    public function __destruct() {
        $this->_conn = null;
    }
}
