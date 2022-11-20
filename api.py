news_data = {
	'news_lenta_ru': {
		'item': 'news_lenta_ru',
		'source': 'https://m.lenta.ru/',
		'object': {'tag': 'li', 'class': 'tabloid__item _mini'},
		'title': {'tag': 'div', 'class': 'card-mini__title'},
		'image': {'tag': 'img', 'class': 'card-mini__image', 'attribute': 'src'},
		'link': {'tag': 'a', 'class': 'card-mini'},
		'integer': {'tag': 'time', 'class': 'card-mini__date'},
		'obj_components': ['titles', 'integers', 'images', 'links']
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
	}	
}

ali_express = {
    'products': {
        'source': 'https://aliexpress.ru',
        'cats_links': {'tag': 'a', 'class': 'snow-ali-kit_Typography__link__1shggo snow-ali-kit_Typography__link__1shggo snow-ali-kit_Typography__strong__1shggo snow-ali-kit_Typography__underline__1shggo SnowCategoriesMenu_CategoryItem__link__1mvfx'},
        'object': {'tag': 'div', 'class': 'product-snippet_ProductSnippet__content__1ettdy'},
        'title': {'tag': 'div', 'class': 'product-snippet_ProductSnippet__name__1ettdy'},
        'integer': {'tag': 'div', 'class': 'snow-price_SnowPrice__mainM__18x8np'},
        'image': {'tag': 'img', 'attribute': 'src'},
        'link': {'tag': 'a', 'class': 'product-snippet_ProductSnippet__galleryBlock__1ettdy'}, 
        'obj_components': ['titles', 'images', 'links', 'integers']
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
        'link': {'tag': 'a'},
        'obj_components': ['titles', 'images', 'integers', 'links']
    },
    'dishes': {
        'source': 'https://klenmarket.ru/shop/tovary-dlia-doma/posuda-dlia-restoranov-i-kafe/',
        'item': 'dishes',
        'cats_links': {'tag': 'a', 'class': 'shop-crockery-list__category-item'},
        'object': {'tag': 'div', 'class': 'shop-crockery__item js-buy-node'},
        'integer': {'tag': 'span', 'class': 'price__current-value'},
        'title': {'tag': 'span', 'class': 'shop-crockery__item-title'},
        'image': {'tag': 'img', 'attribute': 'data-src'},
        'link': {'tag': 'a', 'class': 'shop-crockery__item-head'},
        'obj_components': ['titles', 'images', 'integers', 'links']
    },
    'cutlery': {
        'source': 'https://klenmarket.ru/shop/tovary-dlia-doma/stolovye-pribory/',
        'item': 'cutlery',
        'cats_links': {'tag': 'a', 'class': 'shop-crockery-list__category-item'},
        'object': {'tag': 'div', 'class': 'shop-crockery__item js-buy-node'},
        'integer': {'tag': 'span', 'class': 'price__current-value'},
        'title': {'tag': 'span', 'class': 'shop-crockery__item-title'},
        'image': {'tag': 'img', 'attribute': 'data-src'},
        'link': {'tag': 'a', 'class': 'shop-crockery__item-head'},
        'obj_components': ['titles', 'images', 'integers', 'links']
    },
    # this package works
    'glassware': {
        'source': 'https://klenmarket.ru/shop/tovary-dlia-doma/stekliannaia-posuda/',
        'item': 'glassware',
        'cats_links': {'tag': 'a', 'class': 'shop-eq-list__cats-item'},
        'object': {'tag': 'div', 'class': 'cat-goods__item'},
        'integer': {'tag': 'span', 'class': 'price__current-value'},
        'title': {'tag': 'a'},
        'image': {'tag': 'img', 'attribute': 'data-src'},
        'link': {'tag': 'a'},
        'obj_components': ['titles', 'images', 'integers', 'links']
    },
    # there are some pages on the main one contain other pages with more categories
    'kitchen_utensils': {
        'source': 'https://klenmarket.ru/shop/inventory/kitchen-equipment/',
        'item': 'kitchen_utensils',
        'cats_links': {'tag': 'a', 'class': 'shop-eq-list__cats-item'},
        'object': {'tag': 'div', 'class': 'cat-goods__item'},
        'integer': {'tag': 'span', 'class': 'price__current-value'},
        'title': {'tag': 'a'},
        'image': {'tag': 'img', 'attribute': 'data-src'},
        'link': {'tag': 'a'},
        'obj_components': ['titles', 'images', 'integers', 'links']
    },
    'food_containers': {
        'source': 'https://klenmarket.ru/shop/inventory/kitchen-equipment/gastronorm-containers/',
        'item': 'dood_containers',
        'cats_links': {'tag': 'a', 'class': 'shop-eq-list__cats-item'},
        'object': {'tag': 'div', 'class': 'cat-goods__item'},
        'integer': {'tag': 'span', 'class': 'price__current-value'},
        'title': {'tag': 'a'},
        'image': {'tag': 'img', 'attribute': 'data-src'},
        'link': {'tag': 'a', 'class': 'shop-crockery__item-head'},
        'obj_components': ['titles', 'images', 'integers', 'links']
    },
    'frying_pans': {
        'source': 'https://klenmarket.ru/shop/inventory/kitchen-equipment/pans-cauldrons-saji/',
        'item': 'frying_pans',
        'cats_links': {'tag': 'a', 'class': 'shop-eq-list__cats-item'},
        'object': {'tag': 'div', 'class': 'cat-goods__item'},
        'integer': {'tag': 'span', 'class': 'price__current-value'},
        'title': {'tag': 'a'},
        'image': {'tag': 'img', 'attribute': 'data-src'},
        'link': {'tag': 'a', 'class': 'shop-crockery__item-head'},
        'obj_components': ['titles', 'images', 'integers', 'links']
    },
    'disinfection_means': {
        'source': 'https://klenmarket.ru/shop/tovary-dlia-doma/sredstva-dezinfektsii-i-zashchita/',
        'item': 'disinfection_means',
        'object': {'tag': 'div', 'class': 'cat-goods__item'},
        'integer': {'tag': 'div', 'class': 'price'},
        'title': {'tag': 'a'},
        'image': {'tag': 'img', 'attribute': 'data-src'},
        'link': {'tag': 'a', 'class': 'shop-crockery__item-preview'},
        'obj_components': ['titles', 'images', 'integers', 'links']
    }
}
