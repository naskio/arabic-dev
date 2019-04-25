document.addEventListener('DOMContentLoaded', () => {

    // $('[data-toggle="tooltip"]').tooltip();
    $('.cq-dropdown').dropdownCheckboxes();

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
                    url: $('#res_wrapper').data('url'),
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
                            $('#res_container').empty();
                            data.stemmers.forEach(function (stemmer,index) {
                                $('#res_container').append(renderStemmer(stemmer,index+1));
                            });
                            afterRender();
                            $('#res_wrapper').removeClass('d-none');
                            $('#res_wrapper').addClass('d-block');
                        } else {
                            console.error('error');
                        }
                    })
                    .fail(function (err) {
                        $('#form_text').val('');
                        console.error(err);
                    })
                    .always(function () {
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


function renderStemmer(stemmer,index) {
    return '<div class="col-8 align-self-center">\n' +
        '                <div class="card mt-2 mb-2">\n' +
        '                    <div class="card-header">\n' +
        '                        <h3 class="d-inline mr-3"><span class="badge badge-dark">' + index + '</span></h3>\n' +
        '                        <a href="' + stemmer.url + '" class="text-dark"><h5 class="d-inline mr-3">' + stemmer.display_name + '</h5></a>\n' +
        '                        <a href="' + stemmer.rate_it + '" role="button" class="btn btn-outline-dark">\n' +
        '                            RATE IT\n' +
        '                        </a>\n' +
        '                        <button class="btn btn-dark float-right button_collapse" type="button" data-toggle="collapse"\n' +
        '                                data-target="#' + stemmer.name + '" aria-expanded="true"\n' +
        '                                aria-controls="' + stemmer.name + '">\n' +
        '                            LESS\n' +
        '                        </button>\n' +
        '                    </div>\n' +
        '                    <div class="card-body collapse show" id="' + stemmer.name + '">\n' +
        '                        <p class="text-right" dir="rtl" lang="ar">\n' + stemmer.stemmed +
        '                        </p>\n' +
        '                    </div>\n' +
        '                </div>\n' +
        '            </div>';
}


function afterRender() {
    $('.button_collapse').click(function () {
        $(this).text(function (i, old) {
            return old == 'MORE' ? 'LESS' : 'MORE';
        });
    });
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
