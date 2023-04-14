for(var i = 1; i<=10; i++){

    if(i%2==0){
        console.log(i)
    }

}

    //   0   1    2     3       4     5  
var a = [10 ,30, 50, false, "Hello", "w"];
a.pop(); // deletes "w"
a.pop(); // deletes "hello"
for(var i=0; i<a.length;i++){
    console.log(a[i]);
}
