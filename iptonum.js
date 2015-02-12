function ipToNum(ip) {
  var n = ip.split('.'),bin = []
  for(var i=0;i<4;i++)
    bin[i] = pad(Number(n[i]).toString(2),8)
  return Number(parseInt(bin.join(''),2).toString(10))
}

function numToIp(num) {
	var bin = pad(Number(num).toString(2),32).match(/.{1,8}/g),n = []
	for(var i=0;i<4;i++)
		n[i] = parseInt(bin[i],2).toString(10)
	return n.join('.')
}

function pad(n, width, z) {
  n += '';
  return n.length >= width ? n : new Array(width - n.length + 1).join(z||'0') + n;
}

