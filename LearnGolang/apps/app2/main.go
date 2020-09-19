package main

import (
	"fmt"
	"time"
)

const TimeFormatTplHMS = "2006-01-02 15:04:05"
const TimeFormatTplH =  "2006-01-02 15"
const TimeFormatTpl = "2006-01-02"

func main() {

	end_time := uint32(1592213272)
	start_time := uint32(1592211472)

	fmt.Println(GetBetweenDates(start_time, end_time))
}

func GetBetweenDates(start_time, end_time uint32) []string {
	d := []string{}
	timeFormatTpl := TimeFormatTplHMS
	sdate := time.Unix(int64(start_time), 0).Format(timeFormatTpl)
	edate := time.Unix(int64(end_time), 0).Format(timeFormatTpl)

	if len(timeFormatTpl) != len(sdate) {
		timeFormatTpl = timeFormatTpl[0:len(sdate)]
	}
	date, err := time.Parse(timeFormatTpl, sdate)
	if err != nil {
		return d
	}
	date2, err := time.Parse(timeFormatTpl, edate)
	if err != nil {
		return d
	}
	if date2.Before(date) {
		return d
	}
	timeFormatTpl = TimeFormatTpl
	date2Str := date2.Format(timeFormatTpl)
	date1Str := date.Format(timeFormatTpl)
	// 注意一定要添加这个判断，否则如果传入的时间戳为同一天则会导致死循环
	if date1Str == date2Str {
		d = append(d, date2Str)
		return d
	}
	d = append(d, date.Format(timeFormatTpl))
	for {
		date = date.AddDate(0, 0, 1)
		dateStr := date.Format(timeFormatTpl)
		d = append(d, dateStr)
		if dateStr == date2Str {
			break
		}
	}
	return d
}

