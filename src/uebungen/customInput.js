import { useRef } from 'react';

export function MyInput() {



    const ref = useRef("");
    let x = "Hallo Welt mein Name ist "
    function doClick(event){
        ref.current = event.target.value
        console.log("Ev happeneh" + event.target.value)
        x = event.target.value

        //Span organisieren und reinschreiben
        const my_span =event.target.nextElementSibling
        my_span.innerHTML = event.target.value
    }

    return (<div>Hallo

        <label htmlFor="site-search">Such in der Seite:</label>
        <input
            type="search"
            id="site-search"
            name="q"
            placeholder="Region"
            onChange={doClick}
             />

        <span></span>

        {x} {ref.current} </div>);
}

