#处理滚动条的问题


#滚动到页面最底部就是给的值足够大，页面顶部给0
js="var q=document.documentElement.scrollTop=10000"
driver.execute_script(js)


driver.execute_script("window.scrollTo(0, document.body.scrollHeight*0.5)");


#相对于你当前滚动条位置进行的偏移
driver.execute_script("window.scrollBy(0,200)");

#不管你位置到哪里，移动到绝对的位置
driver.execute_script("window.scrollTo(0, 1500)");