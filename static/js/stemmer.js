document.addEventListener('DOMContentLoaded', () => {

    // HIGHLITING CODE SNIPPETS
    hljs.initHighlightingOnLoad();

    // LOADING TEXT FROM TXT FILE
    $('#import_file').click(function (e) {
        e.preventDefault();
        $('#txt_file').click();
    });
    // STEM ACTION
    const csrftoken = $("[name=csrfmiddlewaretoken]").val();

    $('#form_submit').click(
        function (e) {
            if ($('#form_text').val()) {
                e.preventDefault();
                setLoadingButton();
                $.ajax({
                    url: $('#res_container').data('url'),
                    type: 'post',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    data: JSON.stringify({
                        value: $('#form_text').val(),
                    }),
                    beforeSend: function (xhr) {
                        xhr.setRequestHeader("X-CSRFToken", csrftoken);
                    }
                })
                    .done(function (data) {
                        if (data) {
                            $('#result').html(data.stemmed);
                            $('#diff').html(htmldiff(data.original, data.stemmed));
                            $('#res_container').removeClass('d-none d-flex');
                            $('#res_container').addClass('d-flex');
                        } else {
                            console.error('error');
                        }
                    })
                    .fail(function (err) {
                        $('#form_text').val('');
                        console.error(err);
                    }).always(function () {
                    resetButton();
                });
            }
        }
    );

});

function loadFile() {
    const f_name = document.getElementById("txt_file").files[0];
    if (f_name) {
        const reader = new FileReader();
        if (reader) {
            reader.onload = function (e) {
                if (e.target && e.target.result) {
                    $('#form_text').val(e.target.result);
                }
            };
            reader.readAsText(f_name);
        }
    }
}

function setLoadingButton() {
    $("#form_submit").attr("disabled", true);
    $('#form_submit').empty();
    $('#form_submit').html(
        '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>\n' +
        '  Loading...');
}

function resetButton() {
    $("#form_submit").attr("disabled", false);
    $('#form_submit').empty();
    $('#form_submit').html('STEM');
}
