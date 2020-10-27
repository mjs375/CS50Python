






//let counter = 0;



if (!localStorage.getItem('counter')) { //if NOT something in localstorage called counter...
  localStorage.setItem('counter', 0); //user hasn't visited page yet, needs a 'counter' variable stored locally
}



function count() {
  let counter = localStorage.getItem('counter'); //get user's locally-stored counter
  counter ++;//counter += 1//counter = counter + 1
  //alert(counter); //alert pop-up that display variable 'counter' value
  document.querySelector('h1').innerHTML = counter; //set innerHTML value equal to counter value
  localStorage.setItem('counter', counter); // update counter's value to user's current counter

  if (counter % 10 === 0) {
    alert(`Count is now ${counter}`) // template-literal: substitute value for {variable}. Equivalent to Python's f"{variable}" string
  }
}

document.addEventListener('DOMContentLoaded', function() {
  document.querySelector('h1').innerHTML = localStorage.getItem('counter'); //change HTML page's element to actual counter function on page-load, rather than 0-21,22...
  document.querySelector('button').onclick = count;

    //setInterval(count, 1000); //run count function every 1000ms/1sec

}); //'document' refers to the entire HTML doc. DomContentLoaded: JS only runs after entire contents of page is loaded. Function() is nameless because we are writing it herenow. Anonymous function!


//^^This replaces the Javascript onclick="count()" in the HTML below. This is an Event Listener. It isn't CALLING the function (just count, not count(). This says WHEN and only when the button is clicked, do you run the function. Functions can be treated as values of their own.)
  // This is called Functional Programming.
//document.querySelector returns Null if it can't find something. In this case, the JAvascript code is ABOVE the HTML button/DOM content... so it doesn't think it exists!
