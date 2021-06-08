var user = require('./user')
var fs = require('fs');

var listOfUsers = []

for(let i=0; i<100; i++){
    listOfUsers.push(user.getUser())
}

var dictstring = JSON.stringify(listOfUsers,  null, 2)

fs.writeFile("UsersDataSet.json", dictstring, function(err, result) {
    if(err) console.log('error', err);
});
