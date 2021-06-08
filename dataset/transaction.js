const category = [
    {
        title: "housing",
        percentage: 32.8,
    },
    {
        title: "transportation",
        percentage: 15.9,
    },
    {
        title: "insurance",
        percentage: 11.9,
    },
    {
        title: "health",
        percentage: 8.1,
    },
    {
        title: "groceries",
        percentage: 7.3,
    },
    {
        title: "restraunts",
        percentage: 5.6,
    },
    {
        title: "entertainment",
        percentage: 5.3,
    },
    {
        title: "other",
        percentage: 13.1,
    }
]

function getTransaction () {
    var noOfTransaction = parseInt(Math.random()*25+3); 

    var money = 320+parseInt(Math.random()*320);

    let transaction = [];

    let year = 2000 + parseInt(Math.random()*21)
    let month = parseInt(Math.random()*11)

    for(var i=0; i<noOfTransaction; i++){
        let tempCategory = parseInt(Math.random()*category.length)
        let tempAmount = Math.random()*100*(category[tempCategory]['percentage']/100)
        let transactionDate = 
        transaction.push({
            "date": new Date(year, month, parseInt(Math.random()*30)),
            "amount": tempAmount.toFixed(2),
            "category": tempCategory
        })
    }
    return transaction
}

exports.getTransaction = getTransaction;