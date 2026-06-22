import { type WidgetPlugin, PluginType } from '@deephaven/plugin';
import { type dh } from '@deephaven/jsapi-types';
import { vsWatch } from '@deephaven/icons';
import { PyinstrumentView } from './PyinstrumentView';

export const PyinstrumentPlugin: WidgetPlugin<dh.Widget> = {
  name: '@deephaven/plugin-pyinstrument',
  title: 'Pyinstrument Report',
  type: PluginType.WIDGET_PLUGIN,
  supportedTypes: 'pyinstrument.Report',
  component: PyinstrumentView,
  icon: vsWatch,
};

export default PyinstrumentPlugin;
