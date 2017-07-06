$(document).ready()
			{
				//initiation au parallax
				$('#all .bannerSlider').parallax({imageSrc: 'imgs/TombolaSourdland2016.jpg'});
				//changement de l'allure du header en fonction du scrollTop() écouté au scroll event
				$(window).scroll(function(){
					let scrolled = $(this).scrollTop();
					if(scrolled){
						scrollVerif(scrolled);
					}
				});
				scrollVerif($(window).scrollTop());
				function scrollVerif(scrolled) {
					if(scrolled > 200){
						if($("header").attr("class") == "" || $("header").attr("class") == undefined){
							$("header").addClass("scrolledS0");
						}
					}
					else{
						if($("header").attr("class") == "scrolledS0"){
							$("header").removeClass("scrolledS0");
						}
					}
				}


				function lancer_ecrire(sentence, txt_banner, var_incre) {
					var interval_rajoute_txt = setInterval(function(){
						if(var_incre < sentence.length){
							txt_banner.innerHTML += sentence[var_incre];
							var_incre++;
						}
						else{
							clearInterval(interval_rajoute_txt);
							document.querySelector(".bannerSlider .txtBanner .hr").classList.add("w100hrC");
						}
					}, 100);
				}
				var time_out_ecriture = setTimeout(function(){
					lancer_ecrire("L'association culturelle autour de la langue des Signes      !", document.querySelector(".txtCompleteJs"), 0);
				}, 250);



			}
