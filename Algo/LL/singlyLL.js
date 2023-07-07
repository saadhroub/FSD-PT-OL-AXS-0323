class Node{
    constructor(data){
        this.data = data;
        this.next = null;
    }
}

class SinglyLL{
    constructor(){
        this.head = null;
    }

    print(){
        let current = this.head;
        while(current !=null){
            console.log(current.data);
            current = current.next;
        }
    }

    addFront(data) { 
    let newNode = new Node(data); 
        if(this.head == null) {
            this.head = newNode;
            return this;
        }
        newNode.next = this.head;
        this.head = newNode;
        return this;
    }

    addEnd(data){
    let newNode = new Node(data);
    let current = this.head;
    while(current.next!=null){
        current = current.next;
    }
    current.next = newNode;
    }

    delete(data){
        let previous = this.head;
        let current = previous.next;

        while(current.data != data){
            previous = current;
            current = current.next;
        }
        previous.next = current.next;
        current = null;

    }

    sum(){
        let sum=0;
        let current = this.head;
        while(current!=null){
            sum+=current.data;
            current = current.next;
        }
        return sum;
    }
}

  var myList = new SinglyLL();
  myList.addFront(10);
  myList.addFront(20);
  myList.addFront(30);
  myList.addEnd(100);
  myList.addEnd(5);
  myList.print();
  console.log(myList.sum());


