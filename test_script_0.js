
        (function() {
            let saved = localStorage.getItem('nurselogic_theme') || 'auto';
            let actual = saved === 'auto' ? (window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark') : saved;
            document.documentElement.setAttribute('data-theme', actual);
        })();
    
