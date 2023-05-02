let a = 10;
function f() {
    {
        let b = 9;
        console.log(b);
    } // b will be unaccessible
    console.log(b);
}
f();
console.log(a)