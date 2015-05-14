function VigenèreAutokeyCipher(key, abc) {
  this.encode = function (str) {
  	thiskey = key;
  	var res = '';
  	for(var i=0;i<str.length;i++){
  		if(abc.indexOf(str[i])>-1){
  			var v;
  			var index = abc.indexOf(str[i])
  			var newabc = abc.substring(index,abc.length) + abc.substring(0,index)
  			var start = 0
  			while(thiskey[0] != abc[start])
  				start+=1
  			v = newabc[start]
  			thiskey += str[i]
  			thiskey = thiskey.substring(1,thiskey.length)
  			res+=v
  		}
  		else
  			res += str[i]
  	}
  	return res;    
  };
  this.decode = function (str) {
    var res = '';
    var thiskey = key;
    for(var i=0;i<str.length;i++){
    	if(abc.indexOf(str[i])>-1){
    		var v;
    		var index = abc.indexOf(thiskey[0])
    		var newabc = abc.substring(index,abc.length) + abc.substring(0,index)
    		var start = 0
    		while(str[i] != newabc[start])
    			start+=1
    		v = abc[start]
	    	thiskey += v;
	    	thiskey = thiskey.substring(1,thiskey.length)
	    	res += v;
	    }
	    else
	    	res += str[i];
    }
    return res;
  };
}
var c = new VigenèreAutokeyCipher('PASSWORD', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ');
console.log(c.encode('AAAAAAAAPASSWORDAAAAAAAA') ==  'PASSWORDPASSWORDPASSWORD');
console.log(c.decode('PASSWORDPASSWORDPASSWORD') ==  'AAAAAAAAPASSWORDAAAAAAAA');

var c = new VigenèreAutokeyCipher('password','abcdefghijklmnopqrstuvwxyz')
console.log(c.decode('rovwsoiv') ==  'codewars');
console.log(c.encode('codewars') ==  'rovwsoiv');
console.log(c.encode('waffles') ==  'laxxhsj');
console.log(c.decode('laxxhsj') ==  'waffles');
console.log(c.decode("xt'k s ovzib vapzlz!") ==  "it's a shift cipher!");
console.log(c.encode("it's a shift cipher!") ==  "xt'k s ovzib vapzlz!");

var c = new VigenèreAutokeyCipher('pizza','abcdefghijklmnopqrstuvwxyz')
console.log(c.encode('asodakme') ==  'pancakes');
console.log(c.decode('pancakes') ==  'asodakme');
console.log(c.decode('yiuzslrdpl') == 'javascript');
console.log(c.encode('javascript') == 'yiuzslrdpl');



