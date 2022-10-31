news_data = {
	'news_lenta_ru': {
    	'item': 'news_lenta_ru',
		'source': 'https://m.lenta.ru/',
		'object': {'tag': 'li', 'class': 'tabloid__item _mini'},
		'title': {'tag': 'div', 'class': 'card-mini__title'},
		'image': {'tag': 'img', 'class': 'card-mini__image', 'attribute': 'src'},
		'link': {'tag': 'a', 'class': 'card-mini'},
		'integer': {'tag': 'time', 'class': 'card-mini__date'},
		'obj_components': ['titles', 'integers', 'images','links']
	},
    'news_ria': {
		'item': 'news_ria',
		'source': 'https://ria.ru/',
		'object': {'tag': 'div', 'class': 'cell-list__item m-no-image'},
		'title': {'tag': 'span', 'class': 'cell-list__item-title'},
		'link': {'tag': 'a', 'class': 'cell-list__item-link color-font-hover-only'},
		'integer': {'tag': 'span', 'class': 'elem-info__date'},
		'obj_components': ['titles', 'integers', 'links']
	},
	'news_gazeta_ru': {
		'item': 'news_gazeta_ru',
		'source': 'https://www.gazeta.ru/news/',
		'object': {'tag': 'a', 'class': 'b_ear m_techlisting '},
		'title': {'tag': 'div', 'class': 'b_ear-title'},
		'link': {'tag': 'a', 'class': 'b_ear m_techlisting '},
		'integer': {'tag': 'time', 'class': 'b_ear-time'},
		'image': {'tag': '', 'class': ''},
		'obj_components': ['titles', 'integers', 'links']
	},
	'news_izvestya': {
		'source': 'https://iz.ru/news/',
		'item': 'news_izvestya',
		'object': {'tag': 'a', 'class': 'ticker_item '},
		'title': {'tag': 'div', 'class': 'ticker_item__inside__label__news'},
		'link': {'tag': 'a', 'class': 'ticker_item '},
		'obj_components': ['titles', 'links']
	},
	'weather': {
		'item': 'weather',
		'source': '',
		'object': {'tag': '', 'class': ''}
	},
	'music': {
		'source': 'https://wwv.zvuch.com/',
		'title': {'class': '', 'tag': ''},
		'integer': {'class': '', 'tag': ''},
		'link': {'class': '', 'tag': ''}
	}
}

klen_market = {
    # this package works
    'knives': {
        'source': 'https://klenmarket.ru/shop/tovary-dlia-doma/kukhonnye-nozhi/',
        'item': 'knives',
        'cats_links': {'tag': 'a', 'class': 'shop-eq-list__cats-item'},
        'object': {'tag': 'div', 'class': 'cat-goods__item'},
        'integer': {'tag': 'span', 'class': 'price__current-value'},
        'title': {'tag': 'a'},
        'image': {'tag': 'img', 'attribute': 'data-src'},
        'link': {'tag': 'a', 'class': 'shop-crockery__item-head'},
        'obj_components': ['titles', 'images', 'integers', 'links']
    },
    'dishes': {
        'source': 'https://klenmarket.ru/shop/tovary-dlia-doma/posuda-dlia-restoranov-i-kafe/',
        'cats_links': {'tag': 'a', 'class': 'shop-crockery-list__category-item'},
        'product': {'tag': 'div', 'class': 'shop-crockery__item js-buy-node'},
        'price_for_each': {'tag': 'span', 'class': 'price__current-value'},
        'name': {'tag': 'span', 'class': 'shop-crockery__item-title'},
        'image': {'tag': 'img', 'attribute': 'data-src'},
        'link': {'tag': 'a', 'class': 'shop-crockery__item-head'}
    },
    'cutlery': {
        'source': 'https://klenmarket.ru/shop/tovary-dlia-doma/stolovye-pribory/',
        'cats_links': {'tag': 'a', 'class': 'shop-crockery-list__category-item'},
        'product': {'tag': 'div', 'class': 'shop-crockery__item js-buy-node'},
        'price_for_each': {'tag': 'span', 'class': 'price__current-value'},
        'name': {'tag': 'span', 'class': 'shop-crockery__item-title'},
        'image': {'tag': 'img', 'attribute': 'data-src'},
        'link': {'tag': 'a', 'class': 'shop-crockery__item-head'}
    },
    # this package works
    'glassware': {
        'source': 'https://klenmarket.ru/shop/tovary-dlia-doma/stekliannaia-posuda/',
        'cats_links': {'tag': 'a', 'class': 'shop-eq-list__cats-item'},
        'product': {'tag': 'div', 'class': 'cat-goods__item'},
        'price_for_each': {'tag': 'span', 'class': 'price__current-value'},
        'name': {'tag': 'a'},
        'image': {'tag': 'img', 'attribute': 'data-src'},
        'link': {'tag': 'a', 'class': 'shop-crockery__item-head'}
    },
    # there are some pages on the main one contain other pages with more categories
    'kitchen_utensils': {
        'source': 'https://klenmarket.ru/shop/inventory/kitchen-equipment/',
        'cats_links': {'tag': 'a', 'class': 'shop-eq-list__cats-item'},
        'product': {'tag': 'div', 'class': 'cat-goods__item'},
        'price_for_each': {'tag': 'span', 'class': 'price__current-value'},
        'name': {'tag': 'a'},
        'image': {'tag': 'img', 'attribute': 'data-src'},
        'link': {'tag': 'a', 'class': 'shop-crockery__item-head'}
    },
    'food_containers': {
        'source': 'https://klenmarket.ru/shop/inventory/kitchen-equipment/gastronorm-containers/',
        'cats_links': {'tag': 'a', 'class': 'shop-eq-list__cats-item'},
        'product': {'tag': 'div', 'class': 'cat-goods__item'},
        'price_for_each': {'tag': 'span', 'class': 'price__current-value'},
        'name': {'tag': 'a'},
        'image': {'tag': 'img', 'attribute': 'data-src'},
        'link': {'tag': 'a', 'class': 'shop-crockery__item-head'}
    },
    'frying_pans': {
        'source': 'https://klenmarket.ru/shop/inventory/kitchen-equipment/pans-cauldrons-saji/',
        'cats_links': {'tag': 'a', 'class': 'shop-eq-list__cats-item'},
        'product': {'tag': 'div', 'class': 'cat-goods__item'},
        'price_for_each': {'tag': 'span', 'class': 'price__current-value'},
        'name': {'tag': 'a'},
        'image': {'tag': 'img', 'attribute': 'data-src'},
        'link': {'tag': 'a', 'class': 'shop-crockery__item-head'}
    },
    'disinfection_means': {
        'source': 'https://klenmarket.ru/shop/tovary-dlia-doma/sredstva-dezinfektsii-i-zashchita/',
        'product': {'tag': 'div', 'class': 'cat-goods__item'},
        'price_for_each': {'tag': 'div', 'class': 'price'},
        'name': {'tag': 'a'},
        'image': {'tag': 'img', 'attribute': 'data-src'},
        'link': {'tag': 'a', 'class': 'shop-crockery__item-preview'}
    }
}
