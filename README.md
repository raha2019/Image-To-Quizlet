# Image-Processor-For-Generating-Quizlet
<b>IMPORTANT!</b> : The delimiter detection doesn't work with two termed words that might be found in a textbook like:<b>cash crop</b> farm crop raised to be sold for money(p.97). However, if you want to, you can just edit in the Quizlet import after copying and pasting it into Quizlet. 

<b>Aim</b> : The Aim of the project is to develop a image processor whose output could be input for a Quizlet set.<br />

<b>Input</b> : Any Image with a textbook definition that ends with (). For example: <b>behalf</b> in the interest of(p.204) <br />
<b>Output</b> : Should just be list of words<br /><br />
<b>Pre-requisites</b> :<br />
<b>Modules</b>: Just run Dockerfile <br />
<b>How it works</b>:<br />
<br />1) Upload Image(s) 
<br />2) Tesseract converts images to text 
<br />3) Text is broken up using regex 
<br />4) Delimiter is added 
<br />5) Displays output 
<br />6)(<i>You can refer to [docs](complete_docs) if you need some more help figuring this out</i>)<br /><br />
<b>Result</b> - If everything is run properly, then you should be brought to a page where you will get the final result. If everything looks correct, go ahead and copy and paste it into Quizlet.<br />
<b>Quizlet Processing</b>:
<br /> 1)After copying the result from the Image-Processor, paste it into the Quizlet import 
<br /> 2)Edit anything that needs to be edited 
<br /> 3)Upload to Quizlet 
<br /> 4)Your set has been created with Image-Processor-For-Generating-Quizlet and you are <b>DONE!</b>
