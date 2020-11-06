// J A V A S C R I P T :


document.addEventListener('DOMContentLoaded', function() { // Wait til the DOM Content is completely loaded, then do the following (if-action):
  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);
  // Send email when compose form submitted:
  document.querySelector('#compose-form').onsubmit = submit_compose_form;
  // By default, load the inbox
  load_mailbox('inbox'); // WEBPAGE STARTS HERE BY DEFAULT!
});



function submit_compose_form() {
  // Get email values from form:
  const body = document.querySelector('#compose-body').value;
  const recipients = document.querySelector('#compose-recipients').value;
  const subject = document.querySelector('#compose-subject').value;

  // Send email with form values (call the function)
  send_email(recipients, subject, body);
  return false; //!?!?!?!
}
//
// The above sends data from a submitted form to be processed below:
//
function send_email(recipients, subject, body) {
  // POST request sends email
  event.preventDefault //?!?!
  fetch('/emails', { //fetch the data
    method: 'POST',
    body: JSON.stringify({
      recipients: recipients,
      subject: subject,
      body: body
    })
  })
  .then(response => response.json()) //convert into .json (could be .text, &c.)
  .then(result => {
    console.log(result); //print result
    load_mailbox('sent'); //take user to 'sent' mailbox after submission
  });
}; // END OF SEND_EMAIL * * * * * * * * * * * * * * * * * * * * * * * * *






function compose_email() {
  //
  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#read-email').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';
  //
  // Clear out composition fields
  document.querySelector('#compose-recipients').value = ''; // '' gives users an empty field each time they compose a new email
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
  //
}; // END OF COMPOSE_EMAIL * * * * * * * * * * * * * * * * * * * * * * * * * * * *










function load_mailbox(mailbox) { //'inbox', 'sent', or 'archive' = mailbox (input parameter)
  //
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#read-email').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'none';

  //
  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;
  //
  // Make GET request for emails in ___ mailbox:
  fetch(`/emails/${mailbox}`) //GET request ('emails/inbox/')
  .then(response => response.json()) //json-ify the fetched response
  .then(emails => { //data ... data.emails
    console.log(emails);
    emails.forEach(show_emails); //views.py defines 'emails' as the JsonResponse returned. Loop over all of them, send to show_emails function
  });
  //
} //END OF LOAD_MAILBOX * * * * * * * * * * * * * * * * * * * * *
//
// //
//







function show_emails(emails) { //F(x) will render each email in its own div on the ${mailbox} 'page'
  // Create Mail item to hold ALL emails
  const mail_item = document.createElement('div'); //create container div
  mail_item.className = "mail"; //give each div an id of 'mail'
  mail_item.setAttribute('id', emails.id);
  // Create a row to hold columns (sender, subject, timestamp) of EACH email
  const row = document.createElement('div')
  row.setAttribute('id', `${emails.id}-row`); //row ID is dynamically generated per email.id
  row.setAttribute('class', 'row');
  // {JS if-else ternary:} condition ? expression_if_true : expression_if_false;
  mail_item.style.backgroundColor = emails.read ? '#E0E0E0' : 'white';
  //Create cols for sender/subject/timestamp (+ add attribute + add innerHTML)

  // If Sender inbox, display recipient instead of sender
  const mailbox = document.querySelector('h3').innerHTML;
  console.log(mailbox)
  if (mailbox === "Sent") { //Sent
    //console.log("Created mail_recipients")
    var mail_recipients = document.createElement('div');
    mail_recipients.setAttribute('class', 'col recipient');
    mail_recipients.innerHTML = emails.recipients;
  } else { //Inbox/Archive [ S T A B L E ]
    var mail_sender = document.createElement('div');
    mail_sender.setAttribute('class', 'col sender');
    mail_sender.innerHTML = emails.sender;
  }

  const mail_subject = document.createElement('div');
  mail_subject.setAttribute('class', 'col subject');
  mail_subject.innerHTML = emails.subject;
  const mail_timestamp = document.createElement('div');
  mail_timestamp.setAttribute('class', 'col timestamp');
  mail_timestamp.innerHTML = emails.timestamp;
  // Add the data-filled elements actually into the template!:
  document.querySelector('#emails-view').append(mail_item); //Append the new div into the HTML #emails-view div
  document.getElementById(emails.id).appendChild(row);


  if (mailbox==="Sent") { //Sent
    document.getElementById(`${emails.id}-row`).append(mail_recipients);
  } else { //Inbox/Archive
    document.getElementById(`${emails.id}-row`).append(mail_sender);
  }

  document.getElementById(`${emails.id}-row`).append(mail_subject);
  document.getElementById(`${emails.id}-row`).append(mail_timestamp);
  // When a piece of mail is clicked on, open up that email:
  mail_item.addEventListener('click', () => load_email(`emails/${emails.id}`));
}; // END OF SHOW_MAIL() * * * * * * * * * * * * * * * * * * * * * * * * * * * *




/* STABLE>>OLD COPY OF SHOW_MAILS:
function show_emails(emails) { //F(x) will render each email in its own div on the ${mailbox} 'page'
  // Create Mail items
  const mail_item = document.createElement('div'); //create container div
  mail_item.className = "mail"; //give each div an id of 'mail'
  mail_item.innerHTML = `${emails.sender} - ${emails.subject} - ${emails.timestamp}`; // text-content of the div
  mail_item.style.backgroundColor = emails.read ? '#E0E0E0' : 'white'; //{JS if-else ternary:} condition ? expression_if_true : expression_if_false;
  //
  document.querySelector('#emails-view').append(mail_item); //Append the new div into the HTML #emails-view div
  mail_item.addEventListener('click', () => load_email(`emails/${emails.id}`)); // On-click event listener to mail_item (when clicked, go to view_email f(x) with emails.id in hand...)
}; // END OF SHOW_EMAILS * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*/








function load_email(email) { //page get contents of a single piece of mail
  fetch (email, { //MARK AS READ
    method: 'PUT',
    body: JSON.stringify({
      read: true
    })
  })
  fetch (email)
  .then(response => response.json()) // JSON-ify the single email
  .then(email => {
    console.log(email); //logged in javascript developer console
    read_email(email); // send 'email' data to read_email function
  });
}; // END OF READ_EMAIL * * * * * * * * * * * * * * * * * * * * * * * * *


function read_email(email) {
  // Toggle off all inbox.html div sections besides 'read-email'
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#read-email').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';
  // Add email data to the webpage fields:
  document.querySelector('#email-sender').innerHTML = `${email.sender}`;
  document.querySelector('#email-recipient').innerHTML = `${email.recipients}`;
  document.querySelector('#email-subject').innerHTML = `${email.subject}`;
  document.querySelector('#email-timestamp').innerHTML = `${email.timestamp}`;
  document.querySelector('#email-body').innerHTML = `${email.body}`;

  add_buttons(); // Call function to load archive button:

  document.querySelector('#reply').addEventListener('click', () => reply(email));
  document.querySelector('#archive').addEventListener('click', () => archive(`emails/${email.id}`));


} // END OF READ_EMAIL * * * * * * * * * * * * * * * * * * * * * * * * *

// Autopopulate COMPOSE EMAIL form w/
function reply(email) {
    // Hide other views:
    document.querySelector('#emails-view').style.display = 'none';
    document.querySelector('#read-email').style.display = 'none';
    document.querySelector('#compose-view').style.display = 'block';
    // Clear out composition fields
    document.querySelector('#compose-recipients').value = email.sender;
    // Prevent "RE: RE: RE:" if a reply-to-a-reply...:
    const str = `${email.subject}`;
    var patt = new RegExp("RE:");
    var result = patt.test(str);
    // console.log("Subject:", str, "Pattern:", patt, "Check:", result)
    if (result == false) { // no 're:' yet, add one
      document.querySelector('#compose-subject').value = `RE: ${email.subject}`;
    } else { //if 'true', then don't add another "RE:"
      document.querySelector('#compose-subject').value = `${email.subject}`;
    }
    //
    document.querySelector('#compose-body').value = `On ${email.timestamp} ${email.sender} wrote:\n\n"${email.body}"\n\n- - - - - - - - - - - - - - -\n`;
    // * * * * * * * * * * * *
    document.querySelector('#compose-body').focus() //(Works but autofocuses at bottom of textarea)
}

function add_buttons() { //Dynamically add [un]archive button to HTML
    // Delete existing archive button (remakes it everytime you re-open the email)
    document.getElementById('replarchive-btn-box').innerHTML = ""
    // Determine what inbox you are in: Inbox/Archived
    const mailbox = document.querySelector('h3').innerHTML;

    // If mailbox is 'sent', don't add an reply/archive button at all!
    if (mailbox != "Sent") {
      // Create a button
      const archive_button = document.createElement('button');
      const reply_button = document.createElement('button'); //TEST
      // Assign ID to buttons / assign bootstrap classes
      archive_button.setAttribute('id', 'archive');
      reply_button.setAttribute('id', 'reply'); //TEST
      archive_button.style.display = 'inline-block'; //puts button next to not below other button
      reply_button.style.display = 'inline-block'; //TEST
      archive_button.setAttribute('class', 'btn btn-sm btn-outline-primary');
      // Label button: Archive/Unarchive
      reply_button.setAttribute('class', 'btn btn-sm btn-outline-primary'); //TEST
      archive_button.innerHTML = mailbox==='Inbox' ? 'Archive' : 'Unarchive';
      // Append the new button into the HTML #emails-view div
      reply_button.innerHTML = 'Reply';
      document.querySelector('#replarchive-btn-box').append(reply_button);
      document.querySelector('#replarchive-btn-box').append(archive_button);
    }


} // END OF ARCHIVE_BUTTON() * * * * * * * * * * * * * * *



function archive(email) { // Will TOGGLE on/off (Inbox/Archived mailbox)
  const mailbox = document.querySelector('h3').innerHTML; //name of mailbox
  // If in inbox, archived is false right now; vice-versa with archived email(true)
  const truefalse = mailbox==='Inbox' ? false : true; //condition ? if true:if false. === means equal value & type
  fetch (email, {
    method: 'PUT',
    body: JSON.stringify({
      archived: !truefalse //opposite (NOT) of whatever it was
    })
  })
  .then(email => {
    console.log(email); //logged in javascript developer console
    toast_msg(mailbox);
    load_mailbox('inbox'); //go back to inbox after archiving
    //Add Snackbar/Toast here:(?)
  });
} // END OF ARCHIVE() * * * * * * * * * * * * * * * * * * * * * * * *

//






function toast_msg(mailbox) {
  // Add snackbar div (Archive/Unarchive)
  const toast = document.createElement('div');
  toast.setAttribute('id', 'snackbar'); //TEST
  document.querySelector('#popup').append(toast);
  if (mailbox == "Inbox") {
    document.getElementById('snackbar').innerHTML = "Your email has been archived.";
  } else {
    document.getElementById('snackbar').innerHTML = "Your email has been unarchived.";
  }
  // Get the snackbar DIV
  var x = document.getElementById("snackbar");
  // Add the "show" class to DIV
  x.className = "show";
  // After 3 seconds, remove the show class from DIV
  setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);
} // END OF TOAST() * * * * * * * * * * * * * * * * * * * * * * * * * * * *
