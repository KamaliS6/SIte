// static/scripts.js

document.addEventListener('DOMContentLoaded', function () {
  // Name and Description (Keep this as is - for index.html)
  const nameEl = document.getElementById('name-text');
  const descEl = document.getElementById('description');
  const extraContent = document.getElementById('post-typewriter-content');

  // Only run home-page specific JS if elements exist
  if (nameEl && descEl && extraContent) {
    nameEl.innerHTML = 'Hi, I am Kamali Smith 👋';
    descEl.textContent = "NYC-based Computer Science major and Cybersecurity minor at Fordham University, driven by a love for problem-solving and technology.";

    // Add reveal classes after short delay
    nameEl.classList.add('reveal', 'reveal-1');
    descEl.classList.add('reveal', 'reveal-2');
    extraContent.classList.add('reveal', 'reveal-3');
  }


  // AJAX form submission for contact page (Adjusted)
  const contactForm = document.getElementById('contact-form');
  const messagesContainer = document.getElementById('messages-container'); // Still reference, but won't be used to display past messages
  const flashPlaceholder = document.getElementById('ajax-flash-message');

  // Only run contact-page specific JS if elements exist
  if (contactForm && flashPlaceholder) { // No need to check messagesContainer if not displaying messages

    // NO renderMessageCard function needed as we don't display individual messages

    // NO loadMessages function needed as we don't load past messages

    // NO call to loadMessages() needed on page load


    contactForm.addEventListener('submit', async function (e) {
      e.preventDefault();

      const formData = new FormData(contactForm);

      try {
        const response = await fetch(contactForm.action, {
          method: 'POST',
          credentials: 'same-origin',
          body: formData
        });

        const result = await response.json();

        if (result.success) {
          // No need to render individual message card. Just show the success message.
          contactForm.reset(); // Clear the form
          flashPlaceholder.innerHTML = '<div class="alert alert-success">Message sent successfully!</div>';
        } else {
          flashPlaceholder.innerHTML = `<div class="alert alert-error">${result.error}</div>`;
        }

        // Clear the flash message after a delay
        setTimeout(() => flashPlaceholder.innerHTML = '', 3000); // 3 seconds delay for visibility
      } catch (err) {
        console.error(err);
        flashPlaceholder.innerHTML = '<div class="alert alert-error">Unexpected error.</div>';
        setTimeout(() => flashPlaceholder.innerHTML = '', 3000);
      }
    });
  } // End of contact page specific JS check
});
