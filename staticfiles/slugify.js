//storing inputs into a consta (variable)
//document.querySelector is to search the document
//input[title] and input[slug] are the names when text is entered (look for the inputs)
//inspect the page and click by title and slug. look for 'name' in inspection panel
const titleInput = document.querySelector('input[name=title]');
const slugInput = document.querySelector('input[name=slug]');

const slugify = (val) => {
  return val.toString().toLowerCase().trim()

  //replace text with the Regex Method
  .replace(/&/g,'-and-') //replace & with '-and-'
  .replace(/[\s\W-]+/g,'-') //replace spaces, non word chars, and dashes with a single '-' dash
};
//event listener to see when user types in title field and populate it in slug
titleInput.addEventListener('keyup', (e) => {
  slugInput.setAttribute('value', slugify(titleInput.value));
});
