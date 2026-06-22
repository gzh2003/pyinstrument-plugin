import React, { useEffect, useState } from 'react';
import type { dh } from '@deephaven/jsapi-types';
import { WidgetComponentProps } from '@deephaven/plugin';

export function PyinstrumentView(
  props: WidgetComponentProps<dh.Widget>
): JSX.Element {
  const { fetch } = props;
  const [html, setHtml] = useState<string>();

  useEffect(
    function fetchReport() {
      async function loadReport() {
        const widget = await fetch();
        setHtml(widget.getDataAsString());
      }
      loadReport();
    },
    [fetch]
  );

  return (
    <div
      style={{
        width: '100%',
        height: '100%',
        display: 'flex',
        flexDirection: 'column',
        overflow: 'hidden',
      }}
    >
      {html != null && (
        <iframe
          srcDoc={html}
          title="Pyinstrument Profile Report"
          // allow-same-origin is needed for pyinstrument's HTML to access localStorage
          sandbox="allow-scripts allow-same-origin"
          style={{ width: '100%', height: '100%', border: 'none', flex: 1 }}
        />
      )}
    </div>
  );
}

export default PyinstrumentView;
