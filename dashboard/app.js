(()=>{
  const head=document.head;
  const add=(tag,attrs)=>{const el=document.createElement(tag);Object.entries(attrs).forEach(([k,v])=>el.setAttribute(k,v));head.appendChild(el);return el};
  if(!head.querySelector('link[rel="icon"]')) add('link',{rel:'icon',href:'/favicon.svg',type:'image/svg+xml',sizes:'any'});
  if(!head.querySelector('link[rel="manifest"]')) add('link',{rel:'manifest',href:'assets/site.webmanifest'});
  const css=document.createElement('style');
  css.textContent=`
    .crest,.boot-card .mark{font-size:0!important;color:transparent!important;background:#fff url('assets/raj-urvara-mark.svg') center/86% no-repeat!important;border:1px solid #d6e2ea!important;box-shadow:0 4px 16px rgba(7,62,114,.13)!important}
    .crest{width:42px!important;height:42px!important;border-radius:50%!important;flex:0 0 42px!important}
    .boot-card .mark{border-radius:14px!important;background-size:88%!important}
  `;
  head.appendChild(css);
  const crest=document.querySelector('.crest'); if(crest){crest.setAttribute('aria-label','RAJ-URVARA AI');crest.setAttribute('title','RAJ-URVARA AI');}
  const boot=document.querySelector('.boot-card .mark'); if(boot){boot.setAttribute('aria-label','RAJ-URVARA AI');}
  const core=document.createElement('script');core.src='app-core.js';core.async=false;head.appendChild(core);
})();
