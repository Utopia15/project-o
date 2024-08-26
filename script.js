// You can add JavaScript code here to manipulate the footer elements or add functionality

// Example: Add an event listener to the social media icons to open their respective URLs
document.querySelectorAll('.footer__socials span').forEach((icon) => {
	icon.addEventListener('click', () => {
	  let url = '';
	  switch (icon.querySelector('i').classList[0]) {
		case 'ri-instagram-line':
		  url = '(link unavailable)';
		  break;
		case 'ri-facebook-fill':
		  url = '(link unavailable)';
		  break;
		case 'ri-heart-fill':
		  // You can add a custom URL or functionality for this icon
		  break;
		case 'ri-twitter-fill':
		  url = '(link unavailable)';
		  break;
	  }
	  window.open(url, '_blank');
	});
  });
  
  // Example: Add an event listener to the "Contact Us" email to open the default email client
  document.querySelector('.ri-mail-fill').addEventListener('click', () => {
	window.open('mailto:support@medportal.com');
  });
  
  // Example: Add an event listener to the "Contact Us" phone number to open the default phone dialer
  document.querySelector('.ri-phone-fill').addEventListener('click', () => {
	window.open('tel:+237650047530');
  });
  
