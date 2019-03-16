#!/usr/local/bin/lua

tab1 = {key1 = 'val1', key2 = 'val2', 'val3'}
for k, v in pairs(tab1) do
    print(k .. '--' .. v)
end

print('-----')

tab1.key1 = nil
for k, v in pairs(tab1) do
    print(k .. '--' .. v)
end


-- table
local tbl = {"apple", "pear", "orange", "grape"}
for key, val in pairs(tbl) do
    print("Key", key)
end



-- funcntion

function testFun(tab, fun)
    for k, v in pairs(tab) do
        print(fun(k,v))
    end
end

tab={key1="val1",key2="val2"}

testFun(
    tab, 
    function(key, val)
        return key .. '=' .. val
    end
)


function add(...)  
	local s, arg = 0, {...}  
	for i, v in ipairs(arg) do   --> {...} 表示一个由所有变长参数构成的数组  
		s = s + v  
	end  
	return s, s/#arg, s/select('#', ...)
end  
print(add(3,4,5,6,7))  --->25
