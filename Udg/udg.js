canvas = document.createElement("canvas")
document.body.appendChild(canvas)
document.body.style.margin="0px"
WIDTH = canvas.width = innerWidth
HEIGHT = canvas.height = innerHeight
ctx = canvas.getContext("2d")
ctx.fillRect(0,0,50,50)
PIXEL = 4
bitmap = []
inks=[]
function pixel(n){
	PIXEL = n
}

function ink(letter, color){
	inks.push([letter, color])
}

function create(b,name){
	bitmap.push([b, name])
}

function cls(c){
	ctx.fillStyle = c
	ctx.fillRect(0 ,0 ,WIDTH, HEIGHT)
}

function draw(name, x, y){
	j = 0
	for(b = 0; b < bitmap.length; b++){
		let bit = bitmap[b]
		if(bit[1] == name){
			let row = bit[0]
			for(i = 0; i<row.length; i++){
				letter = row[i]
				for(c = 0; c<inks.length; c++){
					if(letter == inks[c][0]){
						ctx.fillStyle = inks[c][1]
						ctx.fillRect((x + i)*PIXEL, (y+j)*PIXEL, PIXEL, PIXEL)	
					}	
				}
				
			}
			j++
		}
	}
}
