$(document).ready((e)=>{
    // $('[data-toggle="tooltip"]').tooltip();
    $('#original').html(data1.original);
    $('#result').html(data1.result);
    $('#diff').html(htmldiff(data1.original, data1.result));
    // $('.cq-dropdown').dropdownCheckboxes();
});

// document.addEventListener('DOMContentLoaded', () => {
// });
