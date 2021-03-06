const faker = require('faker');
let transaction = require('./transaction');

function getUser () {
    let User = {
        account: faker.finance.account(),
        credential: {
            name: faker.name.findName(),
            email: faker.internet.email()
        },
        account_details: {
            accountName: faker.finance.accountName(),
            routingNumber: faker.finance.routingNumber(),
            mask: faker.finance.mask(),
            amount: faker.finance.amount(),
            transactionType: faker.finance.transactionType(),
            currencyCode: faker.finance.currencyCode(),
            creditCardNumber: faker.finance.creditCardNumber(),
            creditCardCVV: faker.finance.creditCardCVV(),
            iban: faker.finance.iban(),
            bic: faker.finance.bic(),
        },
        transaction: transaction.getTransaction()
    }
    return User
}
exports.getUser = getUser;