var Morse = {};

Morse.encode = function(message){
	var res = message.split('').map(function(x){return x==' '?'0000':Morse.alpha[x]+'000'}).join('').slice(0,-3);
	while(res.length%32!=0) res+='0';
	var chunk = new Array(res.length/32),index=0;
	for(i=0;i<res.length/32;i++,index+=32) chunk[i] = res.slice(index,index+32);
	return chunk.map(function(x){ return x[0]=='0'?parseInt(x.slice(1,32),2):~parseInt(x.slice(1,32).split('').map(function(x){return x=='0'?'1':'0'}).join(''),2)});
};

Morse.decode = function(integerArray){
	var res = integerArray.map(function(x){ y = (x >>> 0).toString(2); while(y.length!=32) y='0'+y; return y;}).join('');
	while(res[res.length-1] != '1') res=res.slice(0,-1);
	var newMorse = Object.keys(Morse.alpha).reduce(function(obj,key){ obj[Morse.alpha[key]] = key; return obj},{});
	return res.replace(/0000000/g,'0000').split(/000/g).map(function(x){ return x[0]=='0'? ' '+newMorse[x.slice(1)] : newMorse[x]}).join('');
};

Morse.alpha = {
  'A': '10111',
  'B': '111010101',
  'C': '11101011101',
  'D': '1110101',
  'E': '1',
  'F': '101011101',
  'G': '111011101',
  'H': '1010101',
  'I': '101',
  'J': '1011101110111',
  'K': '111010111',
  'L': '101110101',
  'M': '1110111',
  'N': '11101',
  'O': '11101110111',
  'P': '10111011101',
  'Q': '1110111010111',
  'R': '1011101',
  'S': '10101',
  'T': '111',
  'U': '1010111',
  'V': '101010111',
  'W': '101110111',
  'X': '11101010111',
  'Y': '1110101110111',
  'Z': '11101110101',
  '0': '1110111011101110111',
  '1': '10111011101110111',
  '2': '101011101110111',
  '3': '1010101110111',
  '4': '10101010111',
  '5': '101010101',
  '6': '11101010101',
  '7': '1110111010101',
  '8': '111011101110101',
  '9': '11101110111011101',
  '.': '10111010111010111',
  ',': '1110111010101110111',
  '?': '101011101110101',
  "'": '1011101110111011101',
  '!': '1110101110101110111',
  '/': '1110101011101',
  '(': '111010111011101',
  ')': '1110101110111010111',
  '&': '10111010101',
  ':': '11101110111010101',
  ';': '11101011101011101',
  '=': '1110101010111',
  '+': '1011101011101',
  '-': '111010101010111',
  '_': '10101110111010111',
  '"': '101110101011101',
  '$': '10101011101010111',
  '@': '10111011101011101',
  ' ': '0' // Technically is 7 0-bits, but we assume that a space will always be between two other characters
};

// note that to test encode, you should test with function that can check similar array
console.log(Morse.encode('HELLO WORLD') === [-1440552402,-1547992901,-1896993141,-1461059584]);
console.log(Morse.decode([-1440552402, -1547992901, -1896993141, -1461059584]) === 'HELLO WORLD');
console.log(Morse.encode('EEEEEEEIE') === [-2004318070,536870912]);
console.log(Morse.decode([-2004318070,536870912]) ===  'EEEEEEEIE');