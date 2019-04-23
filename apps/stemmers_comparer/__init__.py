import swapper


def get_star_ratings_rating_model_name():

    return swapper.get_model_name('stemmers_comparer', 'Rating')


def get_star_ratings_rating_model():

    return swapper.load_model('stemmers_comparer', 'Rating')

