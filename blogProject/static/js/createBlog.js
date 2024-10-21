// CKEditor5 config
const config = {
  toolbar: [
    "heading",
    "|",
    "bold",
    "italic",
    "link",
    "bulletedList",
    "numberedList",
    "blockQuote",
    "|",
    "insertTable",
  ],
};

window.ClassicEditor.create(document.querySelector(".content"), config).catch(
  (error) => {
    console.error(error);
  }
);

// Handling categories
const categoryField = document.querySelector(".cate-field");
const templateField = categoryField.cloneNode(true);

document.querySelector(".add-new-cate").addEventListener("click", (e) => {
  e.preventDefault();
  const cloneField = templateField.cloneNode(true);
  document.querySelector(".cate-list").appendChild(cloneField);

  // HANDLING DELETE CATEGORY
  document.querySelectorAll(".delete-btn").forEach((deleteBtn) => {
    deleteBtn.addEventListener("click", (e) => {
      e.preventDefault();
      const removedCate = deleteBtn.closest(".cate-field");
      console.log(removedCate);
      if (removedCate) {
        removedCate.remove();
      } else {
        console.error("There has been an error deleting a category");
      }
    });
  });
});
