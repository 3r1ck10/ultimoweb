$(function(){
/* BASE */

	/* FECHA FOOTER */
	var fecha = new Date();
	var ano =fecha.getFullYear();
	$('#id_year').text(ano)

	/* MENU RESPONSIVE */
	//se clona 'menu-list' para poder tener mas flexibilidad y control
	$('.menu-list').clone().appendTo('.menu-sidebar-cnt').addClass('menu-responsive').removeClass('menu-list');
	$('.header-logo').clone().prependTo('.menu-sidebar-cnt').removeClass('header-logo').addClass('responsive-logo');
	$('.header-form').clone().appendTo('.menu-sidebar-cnt');

	$('.-head-info').clone().appendTo('.clone-info-head');

	$('.menu-mobile-open').click(function(){
		$(this).addClass('active');
		$('.menu-mobile-close').addClass('active');
		$('.menu-sidebar').addClass('active');
		$('.menu-overlay').addClass('active');
		$('.cnt-wrapper').addClass('active');
		$('.footer').addClass('active');
		$('body').addClass('active');
	});

	// funcion  para cerrar menu responsive
	function cerrar_nav() {
		$('.menu-sidebar').removeClass('active');
		$('.menu-overlay').removeClass('active');
		$('.menu-mobile-close').removeClass('active');
		$('.menu-mobile-open').removeClass('active');
		$('.cnt-wrapper').removeClass('active');
		$('.footer').removeClass('active');
		$('body').removeClass('active');
	};

	//click en boton cerrar y overlay
	$('.menu-mobile-close').click(function() {
		cerrar_nav();
	});

	$('.menu-overlay').click(function() {
		cerrar_nav();
	});


	//para cerrar el menu responsive en caso hagan resize, o giren la tablet o celular con el menu responsive abierto
		//detectando moviendo de ipad y tablet
	function readDeviceOrientation() {
	    switch (window.orientation) {
	    case 0:
	        break;
	    case 180:
	        break;
	    case -90:
	        break;
	    case 90:
	        break;
	    }
	}
	//detectando tablet, celular o ipad
	dispositivo_movil = $.browser.device = (/android|webos|iphone|ipad|ipod|blackberry|iemobile|opera mini/i.test(navigator.userAgent.toLowerCase()))

	if ( dispositivo_movil ) {
			function readDeviceOrientation() {
			    if (Math.abs(window.orientation) === 90) {
			        // Landscape
			      	cerrar_nav();
			    } else {
			    	// Portrait
			    	cerrar_nav();
			    }
			}
			window.onorientationchange = readDeviceOrientation;
	}else{
		$(window).resize(function(event) {
			var estadomenu = $('.menu-responsive').width();
			if(estadomenu != 0){
				cerrar_nav();
			}
		});
	};
	//Detectando navegador
		$.browser.chrome = /chrome/.test(navigator.userAgent.toLowerCase());

		/* Detect Chrome */
		if($.browser.chrome){
			/* Do something for Chrome at this point */
			// alert("You are using Chrome!");

			/* Finally, if it is Chrome then jQuery thinks it's
			   Safari so we have to tell it isn't */
			$.browser.safari = false;
		}

		/* Detect Safari */
		if($.browser.safari){
			/* Do something for Safari */
			// alert("You are using Safari!");
		}






	// Ancla scroll - AGREGAR CLASE DEL ENLACE
	$('miclase[href*=#]').click(function() {
	if(location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'')&& location.hostname == this.hostname) {
			var $target = $(this.hash);
			$target = $target.length && $target || $('[name=' + this.hash.slice(1) +']');
			if ($target.length) {
			var targetOffset = $target.offset().top;
			$('html,body').animate({scrollTop: targetOffset}, 1000);
			return false;
			}
		}
	});

	// Reseteando cajas de texto administrables
	$('.no-style *').removeAttr('style');


	// Menu responsive traslucido con scrolling
	var altoScroll = 0
	$(window).scroll(function() {
		altoScroll = $(window).scrollTop();
		if (altoScroll > 60) {
			$('.menu-mobile-open').addClass('scrolling');
		}else{
			$('.menu-mobile-open').removeClass('scrolling');
		};
	});


	// controlar los placeholde
	$('input, textarea').placeholder();


	// buscador-header
	$('.js-open-search').click(function(e) {
		e.preventDefault();
		$('.header-buscador-cnt').slideToggle();
	});

	$('.js-close').click(function(e) {
		e.preventDefault();
		$('.header-buscador-cnt').hide();
	});

	$('.click-b15').click(function(event) {
       $('.b15-cnt').addClass('active');
       $('.b15-elent-gracias').addClass('active');
    });

	$('.jsb15-open-fancy, .jsb15-open-fancy-compartir').click(function(event) {
       $('.b15-cnt').removeClass('active');
       $('.b15-elent-gracias').removeClass('active');
    });


/* --- FIN BASE --- */
});
