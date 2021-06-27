# CAUTION: The code is more spaghetti than those made by Italians. View at your own risk.

## How to run this program?

Simple. Just use Python 3 to run `main.py`  

## What's the input format?

Input should consist of 2 part. The hand and the calls. And they should be seperated by spaces.  

### The hand
The hand is a string you would type on [Tenhou](https://tenhou.net/2/img/) to generate your hand.  
For example:  
```
19m19p19s1234567z1p
123m4477p789s222z4p
```
### The calls
The call is a bit different. It uses a way of repersentation I think myself becau I was too lazy to Google it.  
The syntax look like this:  
`<type><from who><tile(s)> `  
followed by a space.  
`type` can be one of `c`(chi), `p`(pon), `ka`(ankan), `kk`(kakan), `km`(daiminkan).  
`from who` can be one of `l`(left), `m`(middle), `r`(right). `from who` is not needed when `type` is `ka`.
`tile` is just like the hand but:  
when `type` is `c` you type 3 numbers followed by a color like `cl123m` and `cm456p`.  
otherwise you just need 1 tile like `pr4s`, `ka5z`, `kml6p`.  
  
This is what `11s pl1z ka2z kmr3z kkm4z` outputs.  
![example]("./11s pl1z ka2z kmr3z kkm4z.png")