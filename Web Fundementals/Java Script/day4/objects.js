var student1 = {
  "firstName": "Saad",
  "age": 20,
  "weight": 75,
  "greetings": function () {
    console.log("Welcome to Java Script");
  },


  "college": {
    "collegeName": "Birzeit",
    "joinDate": 2023,
    "major": "marketing"
}
};

var student2 = {
  "firstName": "Hussein",
  "age": 22,
  "weight": 70,
 "greetings": function () {
    console.log("Welcome to Java Script");
  },
};

student1.firstName = "Saadeddin";

console.log(student1.college.collegeName);
student1.greetings();
console.log(student2.firstName);
student2.greetings();

