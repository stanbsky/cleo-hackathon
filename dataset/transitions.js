var noOfTransaction = parseInt(Math.random()*25+3); 

var money = 100;
transaction = [];

for(var i=0; i<noOfTransaction; i++){
    transaction.push({
        "date": Date.now(),
        "amount": parseFloat(Math.random()*100).toFixed(2),
        "category": parseInt(Math.random()*5)
    })
}
console.log(transaction);
console.log(noOfTransaction);
