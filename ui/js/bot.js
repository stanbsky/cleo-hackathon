var botui = new BotUI('my-botui-app');

botui.message.add({
    delay: 500,
    loading: true,
    content: 'Hello from bot.'
}).then(function () { // wait till its shown
    botui.message.add({ // show 'text' action
        delay: 500,
        loading: true,
        human: true,
        type: 'html',
        content: '!(check) Hello from bot.'
    });
})

botui.action.text({
    addMessage: false,
    action: {
        placeholder: 'Your name'
    }
}).then(function (res) { // will be called when a button is clicked.
    botui.message.add({
        human: true, // show it as right aligned to UI
        content: 'My name is ' + res.value
    });
});