
(function(){
  var topBtn=document.querySelector('.eralux-floating__top');
  if(topBtn){window.addEventListener('scroll',function(){topBtn.classList.toggle('is-visible',window.scrollY>420)});topBtn.addEventListener('click',function(){window.scrollTo({top:0,behavior:'smooth'})});}
  document.querySelectorAll('.case').forEach(function(card){card.addEventListener('click',function(e){if(window.matchMedia('(max-width: 767px)').matches && !e.target.closest('.case__overlay-actions')){card.classList.toggle('is-open');}})});
  document.querySelectorAll('[data-filter]').forEach(function(btn){btn.addEventListener('click',function(){var f=btn.getAttribute('data-filter');document.querySelectorAll('[data-filter]').forEach(function(b){b.classList.toggle('is-active',b===btn)});document.querySelectorAll('.case[data-cat]').forEach(function(c){c.style.display=(f==='all'||(c.getAttribute('data-cat')||'').indexOf(f)>=0)?'':'none';});});});
  var paletteModal=document.querySelector('.palette-modal');
  if(paletteModal){
    var modalSwatch=paletteModal.querySelector('.palette-modal__swatch');
    var modalFinish=paletteModal.querySelector('.palette-finish-badge');
    var modalNumber=paletteModal.querySelector('.palette-modal__number');
    var modalDescription=paletteModal.querySelector('.palette-modal__description');
    function closePalette(){paletteModal.setAttribute('aria-hidden','true');document.body.classList.remove('palette-modal-open');}
    document.addEventListener('click',function(e){
      var card=e.target.closest('.eralux-palette-card');
      if(!card){return;}
      e.preventDefault();
      var number=card.getAttribute('data-palette-number');
      var description=card.getAttribute('data-palette-description');
      var base=card.getAttribute('data-palette-base');
      var shadow=card.getAttribute('data-palette-shadow');
      var highlight=card.getAttribute('data-palette-highlight');
      var finish=card.getAttribute('data-palette-finish')||'matte';
      var finishLabel=card.getAttribute('data-palette-finish-label')||finish;
      if(modalSwatch){
        modalSwatch.style.setProperty('--swatch-base',base||'#c8c3b8');
        modalSwatch.style.setProperty('--swatch-shadow',shadow||'#8f887c');
        modalSwatch.style.setProperty('--swatch-highlight',highlight||'#f8f4eb');
        modalSwatch.classList.toggle('palette-card--glossy',finish==='glossy');
        modalSwatch.classList.toggle('palette-card--matte',finish!=='glossy');
      }
      if(modalFinish){modalFinish.textContent=finishLabel;}
      modalNumber.textContent=number||'';
      modalDescription.textContent=description||'';
      paletteModal.setAttribute('aria-hidden','false');
      document.body.classList.add('palette-modal-open');
    },true);
    paletteModal.querySelectorAll('[data-palette-close]').forEach(function(btn){btn.addEventListener('click',closePalette);});
    document.addEventListener('keydown',function(e){if(e.key==='Escape'){closePalette();}});
  }
})();
