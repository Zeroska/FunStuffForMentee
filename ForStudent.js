

function isArmStrong(number){
	let total = 0
	let temp = number 
	while(temp != 0){
		let digit = temp%10
		total += digit**3
		temp = parseInt(temp/10) 
	}	
	if (total == i){
		return true
	}
	return false 
}


let result = ""
let i  = 1
while(i<999){
	let kq = isArmStrong(i)
	if (kq  == true){
		result += i + " ";
	}
	i++
}
console.log(result)



const Node = ()=>{
	this.data = {} 
	this.next = null
}

const LinkedList = ()=>{
	this.head = null 
}


LinkedList.prototype.addHead = (Node)=>{
	if(this.head == null){
		this.head = node 
		
	}
	else{
		node.next = this.head
		this.head = node 	
	}
}

LinkedList.prototype.printList = ()=>{
	let current = this.head
	while(current != null){
		console.log(current)
		current = current.next 
	}
}





