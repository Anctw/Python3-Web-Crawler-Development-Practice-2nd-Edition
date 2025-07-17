Java.perform(() => {
    let MainActivity = Java.use("com.germey.appbasic1.MainActivity")
    
    // let MainActivity = Java.use("com.germey.")
    console.log("start hook")
    MainActivity.getMessage.implementation = (arg1, arg2) => {
        send("Start Hook!")
        return '6'
    }
})