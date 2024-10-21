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

const categoryField = document.querySelector(".cate-field");
const templateField = categoryField.cloneNode(true);

// CATEGORIES
document.querySelector(".add-new-cate").addEventListener("click", (e) => {
  e.preventDefault();
  const cloneField = templateField.cloneNode(true);
  document.querySelector(".cate-list").appendChild(cloneField);
});

// Find and remove the closest cate-field
document.querySelectorAll(".delete-btn").forEach((deleteBtn) => {
  deleteBtn.addEventListener("click", (e) => {
    e.preventDefault();
    const removedCate = deleteBtn.closest(".cate-field");
    if (removedCate) {
      removedCate.remove();
    } else {
      console.error("There has been an error deleting a category");
    }
  });
});
