let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"]

console.log(users.length)
if (users.length == 0){
    console.log("No one is online")
}
if( users.length ==1){
    console.log(users[0] + " is online")
}
if( users.length ==2){
    console.log(users[0] + " and" +
    users[1] + " are online")
}
if ( users.length > 2){
    let n =users.length - 2
    console.log(users[0] + ", " + users[1] + " and " + n + " more are online")
}