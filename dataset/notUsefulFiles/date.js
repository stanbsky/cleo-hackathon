var date = new Date(2002, 11, 1)
var dateToBeSub = Date.now()
var value = Math.abs(date - dateToBeSub);
console.log(dateToBeSub)
console.log(new Date(date))
console.log(dateToBeSub)
console.log(value)