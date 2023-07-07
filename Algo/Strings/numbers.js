var str1 = "P5@5wwqertyuio888kjhfdskjgf7770rd";
var str2="";
for(var i=0; i<str1.length;i++){
    if(isNaN(str1[i])==false){
        str2+=str1[i];
    }
}
console.log(Number(str2));