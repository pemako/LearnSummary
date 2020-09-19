package main

import (
	"fmt"

	_ "github.com/go-sql-driver/mysql"
	"github.com/jmoiron/sqlx"
)

// 因为统计的数据均为聚合的数据故这里不仅有按照项目和时间维度的字段
type Trace struct {
	Id          uint32 `db:"id"`
	ProjectId   uint32 `db:"project_id"`
	Day         uint32 `db:"day"`
	Hr          uint32 `db:"hr"`
	Uid         string `db:"uid"`
	EnvId       uint32 `db:"env_id"`
	Callee      string `db:"callee"`
	Caller      string `db:"caller"`
	Function    string `db:"function"`
	TotalNum    uint32 `db:"total_num"`
	ReqTotalNum uint32 `db:"req_total_num"`
	ProxyErrNum uint32 `db:"proxy_err_num"`
	BusiErrNum  uint32 `db:"busi_err_num"`
}

func main() {

	traces := make([]Trace, 0)

	db, err := sqlx.Open("mysql", "root:vjzHn)3284ev@tcp(9.134.33.87:3306)/envops?charset=utf8mb4")
	defer db.Close()

	if err != nil {
		fmt.Println(err.Error())
	}

	err = db.Select(&traces, "select id, project_id, day, hr, uid, env_id, caller, callee from trace limit 2")

	if err != nil {
		fmt.Println(err.Error())
	}

	tx, err := db.Begin()
	tx.Exec("UPDATE trace t, env_srvc_ins e SET t.env_id = e.`env_id` where t.`day` = ? and t.`hr` = ?  and t.`caller` = e.`srvc_ins_name`", 1593331200, 16)
	tx.Commit()

	/*
		if err != nil {
			fmt.Println(err.Error())
		}

		i, err := res.RowsAffected()

		fmt.Println(i)

		if err != nil {
			fmt.Println(err.Error())
		}
	*/
}
