import React, { useRef, useEffect } from "react";

const { tableau } = window;

const TableauScoresEmbed = React.forwardRef((props, ref) => {
    const dref = useRef(null);
    const url = "https://public.tableau.com/shared/RMYZPXWW7?:display_count=n&:origin=viz_share_link";

    function initViz () {
        new tableau.Viz(ref.current, url);
    }
    useEffect(() => {
        initViz();
    }, [])
    return (
        <div ref={ref}>
            <div ref={dref}></div>
        </div>
    );
});



export default TableauScoresEmbed;