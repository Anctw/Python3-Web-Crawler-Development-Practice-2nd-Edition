// 修改前
// Java.perform(() => {
//     let MainActivity = Java.use("com.germey.appbasic2.MainActivity")
//     console.log("start hook")
//     MainActivity.getMessage.implementation = (arg1, arg2) => {
//         send("Start Hook!")
//         return '6'
//     }
// })


//修改后
Java.perform(() => {
    Interceptor.attach(Module.findExportByName('libnative.so', 
        'Java_com_germey_appbasic2_MainActivity_getMessage'),{
            onEnter: function (args) {
                send('hook onEnter')
                send('args[1]=' + args[2])
                send('args[2]=' + args[3])
            },
            onLeave: function (val){
                send('hook save')
                val.replace(Java.vm.getEnv().newStringUtf('5'))
            }
        })
})