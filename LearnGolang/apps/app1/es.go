package main

import (
	"context"
	"encoding/json"
	"fmt"
	"github.com/olivere/elastic/v7"
	"math"
	"strconv"
	"strings"
	"time"
)

// Span is the database representation of a span.
type Span struct {
	TraceID       string
	SpanID        string
	Flags         uint32
	OperationName string
	StartTime     uint64
	Duration      uint64
	Tags          []*KeyValue
	Logs          []*Log
	References    []*SpanRef
	Process       *Process
	ServiceName   string
}

// KeyValue is the UDT representation of a Jaeger KeyValue.
type KeyValue struct {
	Key   string
	Type  string
	Value interface{}
}

// Log is the UDT representation of a Jaeger Log.
type Log struct {
	Timestamp uint64
	Fields    []KeyValue
}

// SpanRef is the UDT representation of a Jaeger Span Reference.
type SpanRef struct {
	RefType string
	TraceID string
	SpanID  string
}

// Process is the UDT representation of a Jaeger Process.
type Process struct {
	ServiceName string
	Tags        []KeyValue
}

func getSpanFromElastic() {
	//client, err := elastic.NewClient(elastic.SetURL("http://localhost:9200"),elastic.SetBasicAuth("elastic","09Hu9SzKC80z2oI52YHVr67E"))
	client, err := elastic.NewClient(elastic.SetURL("http://localhost:9200"), elastic.SetBasicAuth("elastic", "09Hu9SzKC80z2oI52YHVr67E"))
	if err != nil {
		panic(err)
	}
	defer client.Stop()

	//names, err := client.IndexNames()
	if err != nil {
		panic(err)
	}
	start_time := int32(1591286400)

	fmt.Println(uint64(start_time)*1000000)

	rangeQuery := elastic.NewRangeQuery("startTime").From(1591286400000000).To(1591286400900000)


	boolQuery := elastic.NewBoolQuery()
	tpro := elastic.NewTermQuery("tags.key", "mako-0003")
	tpro1 := elastic.NewTermQuery("tags.value", "13")
	tpro2 := elastic.NewTermQuery("tags.key", "project_id")
	tpro3 := elastic.NewTermQuery("tags.value", "1000")

	proNest := elastic.NewNestedQuery("tags", tpro)
	proNest1 := elastic.NewNestedQuery("tags", tpro1)
	proNest2 := elastic.NewNestedQuery("tags", tpro2)
	proNest3 := elastic.NewNestedQuery("tags", tpro3)
	boolQuery.Must(proNest1).Must(proNest2).Must(proNest3)

	boolQuery.Must(proNest).Must(rangeQuery)
	//boolQuery.Must(rangeQuery)
	//q := elastic.NewMatchQuery("tags.key", "client-uuid")
	//q := elastic.NewTermQuery("tags.key", "client-uuid")
	//nq := elastic.NewNestedQuery("tags", q)

	//boolQuery.Must(rangeQuery).Must(q)
	searchResult, err := client.Search().
		Index("jaeger-span-2020-06-06").
		Query(boolQuery).
		From(0).Size(10).
		Pretty(true).
		Do(context.Background())          // execute
	if err != nil {
		// Handle error
		panic(err)
	}

	//aa, _ :=client.Search().Index("jaeger-span-2020-05-21").Source("tags.key:param.driverID").From(0).Size(1).Do(ctx)
	//fmt.Println(aa)

	// 获取总共查询出来的数据总数
	fmt.Printf("Found a total of %d tweets\n", searchResult.TotalHits())
	//var t, t1 Span
	var loopNum = int(math.Ceil(float64(searchResult.TotalHits()) / 500))
	fmt.Println(loopNum)
	//var totalNum = 0
	//if searchResult.Hits.TotalHits.Value > 0 {
	//	//noinspection GoBinaryAndUnaryExpressionTypesCompatibility
	//	for i := 0; i < loopNum; i++ {
	//		searchResult, err = client.Search().Index("jaeger-span-2020-05-21").From(i * 1).Size(1).Pretty(true).Do(ctx)
	//		// 获取总共查询出来的数据总数
	//		for _, item := range searchResult.Each(reflect.TypeOf(t)) {
	//			t := item.(Span)
	//			fmt.Println(t.SpanID, t)
	//			totalNum += 1
	//		}
	//	}
	//	fmt.Println("totalNum", totalNum)
	//}

		if searchResult.Hits.TotalHits.Value > 0 {
			for _, hit := range searchResult.Hits.Hits {
				fmt.Println(string(hit.Source))
			}
		} else {
			// No hits
			fmt.Print("Found no tweets\n")
		}

	return
}



func genUniqKeyForSpan() string {
	var byt = `{
    "traceID":"e787055283fa9a3305da2fe9716497b4",
    "spanID":"05da2fe9716497b4",
    "operationName":"/mini_app_dcreport/DcReport",
    "startTime":1591084672696326,
    "duration":1487,
    "tags":[
        {
            "key":"function",
            "type":"string",
            "value":"/mini_app_dcreport/DcReport"
        },
        {
            "key":"project_id",
            "type":"string",
            "value":"12"
        },
        {
            "key":"proxy_err",
            "type":"string",
            "value":"-"
        },
        {
            "key":"caller",
            "type":"string",
            "value":"envops-mini-admin-access"
        },
        {
            "key":"cluster_id",
            "type":"string",
            "value":"cls-iw1n147m"
        },
        {
            "key":"env_id",
            "type":"string",
            "value":""
        },
        {
            "key":"http_method",
            "type":"string",
            "value":"POST"
        },
        {
            "key":"http_status_code",
            "type":"string",
            "value":"200"
        },
        {
            "key":"http_url",
            "type":"string",
            "value":"/mini_app_dcreport/DcReport"
        },
        {
            "key":"route_key",
            "type":"string",
            "value":"421031267"
        },
        {
            "key":"callee",
            "type":"string",
            "value":"envops-mini-app-dcreport"
        },
        {
            "key":"error",
            "type":"bool",
            "value":false
        },
        {
            "key":"http_host",
            "type":"string",
            "value":"svc-mini-app-dcreport"
        },
        {
            "key":"peer.service",
            "type":"string",
            "value":"envops-mini-app-dcreport"
        },
        {
            "key":"peer.ipv4",
            "type":"string",
            "value":"9.148.204.63"
        },
        {
            "key":"span.kind",
            "type":"string",
            "value":"client"
        },
        {
            "key":"internal.span.format",
            "type":"string",
            "value":"zipkin"
        }
    ]}`

	var span Span
	err := json.Unmarshal([]byte(byt), &span)
	if err != nil {
		fmt.Println(err)
		return err.Error()
	}
	fmt.Println(span.Tags)

	/*
		遍历span数据 以
			- project_id, env_id, uid, caller, callee, function, day, hr 作为key
				- project_id 取 tags.project_id
				- env_id 取 tags.env_id
				- caller 取 tags.caller
				- callee 取 tags.callee
				- function 取 tags.function
				- dt hr span的索引为准
			- 有一条数据 total_num +1
			- tags.error = true 则 req_err_num +1
			- proxy_err = true  则  proxy_err_num +1
			- busi_err= ture 则 busi_err_num +1
	*/

	//_project_id := fmt.Sprintf("%v", getKeyFromTag("project_id", span))
	//_env_id := fmt.Sprintf("%v", getKeyFromTag("env_id", span))
	//_callee := fmt.Sprintf("%v", getKeyFromTag("callee", span))
	//_caller := fmt.Sprintf("%v", getKeyFromTag("caller", span))
	//_function := fmt.Sprintf("%v", getKeyFromTag("function", span))
	//
	//_error := fmt.Sprintf("%v", getKeyFromTag("error", span))
	//
	//fmt.Println(_error)
	//_s := []string{_project_id, _env_id, _callee, _caller, _function}
	//
	//
	//t := reflect.TypeOf(getKeyFromTag("project_id", span))
	//v := reflect.ValueOf(getKeyFromTag("project_id", span))
	//fmt.Println("----->>>", t, v)
	//
	//
	//key := strings.Join(_s, "|")
	//fmt.Println(key)
	v := getKeyFromTag(span)
	fmt.Println(strings.Join(v, "|"))
	return ""
}

func getValueFromTag(k string, s Span) string {
	_v := ""
	for _, v := range s.Tags {
		if v.Key == k {
			if v.Type == "bool" {
				_v = strconv.FormatBool(v.Value.(bool))
			} else {
				_v = v.Value.(string)
			}
			break
		}
	}
 	return _v
}

func getKeyFromTag(s Span) []string {
	_needKey := []string{"project_id", "env_id", "callee", "caller", "function", "error", "proxy_err", "busi_err"}
	_getValue := []string{}
	for _, v := range _needKey {
		_v := getValueFromTag(v, s)
		_getValue = append(_getValue, _v)
	}
	fmt.Println(_getValue)
	return _getValue
}



func parseWithLocation(name string, timeStr string) (time.Time, error) {
	locationName := name
	if l, err := time.LoadLocation(locationName); err != nil {
		return time.Time{}, err
	} else {
		lt, _ := time.ParseInLocation("2006-01-02 15", timeStr, l)
		return lt, nil
	}
}

func main() {

	//a := `{"traceID":"mako0000002","spanID":"mako0000002","operationName":"/mini_app_dcreport/DcReport","startTime":1591286400200000,"duration":1487,"tags":[{"key":"project_id","type":"string","value":"13"},{"key":"env_id","type":"string","value":"1000"},{"key":"error","type":"bool","value":false},{"key":"proxy_err","type":"bool","value":false},{"key":"busi_err","type":"bool","value":false},{"key":"caller","type":"string","value":"envops-mini-admin-access"},{"key":"callee","type":"string","value":"envops-mini-app-dcreport"},{"key":"function","type":"string","value":"/mini_app_dcreport/DcReport"},{"key":"peer.service","type":"string","value":"envops-mini-app-dcreport"},{"key":"peer.ipv4","type":"string","value":"9.148.204.63"},{"key":"mako-0003","type":"string","value":"cls-iw1n147m"}]}`
	//
	//b := strings.ReplaceAll(a, "false", "\"false\"")
	//
	//var _span Span
	//fmt.Println([]byte(b))
	//
	//err := json.Unmarshal([]byte(b), &_span)
	//if err != nil {
	//	fmt.Println(err.Error())
	//}
	//fmt.Println(_span)
	//t  := reflect.TypeOf(a)
	//fmt.Println(a,b, t)
	//genUniqKeyForSpan()
	//getSpanFromElastic()
	// 2020-06-06 00:05:00

	timestamp := 1591373100 - 3600
	timeFormatTpl := "2006-01-02 15"
	sdate := time.Unix(int64(timestamp), 0).Format(timeFormatTpl)
	_tmp := strings.Split(sdate, " ")
	index, hr := _tmp[0], _tmp[1]
	fmt.Println(index, hr)

	//// 获取当前小时的开始时间戳和结束时间戳
	//date2, err := time.Parse("2006-01-02 15", sdate)
	//if err != nil {
	//	fmt.Println("AAA")
	//}
	//fmt.Println(date2, date2.Unix())

	date3, _ := parseWithLocation("Asia/Shanghai", sdate)
	startTime := date3.Unix()
	endTime := startTime + 3600
	fmt.Println(startTime, endTime)
}

