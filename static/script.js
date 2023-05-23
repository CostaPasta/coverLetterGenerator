var myVar;

function myFunction() {
  myVar = setTimeout(showPage, 3000);
}

function showPage() {
  document.getElementById("loader").style.display = "none";
  document.getElementById("myDiv").style.display = "block";
}

function copyToClipboard() {
    const textToCopy = document.getElementById('cover-letter-content').innerText;
  
    navigator.clipboard.writeText(textToCopy)
      .then(() => {
        alert('Text copied to clipboard!');
      })
      .catch((error) => {
        console.error('Failed to copy text: ', error);
      });
  }
  