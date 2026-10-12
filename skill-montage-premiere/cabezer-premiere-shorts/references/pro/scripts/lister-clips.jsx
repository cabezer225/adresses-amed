// lister-clips.jsx : lecture seule (ExtendScript, a tester). Signale hors ligne, desactives, trous video, pistes audio.
var TICKS = 254016000000, seq = app.project.activeSequence, rep = [];
var fr = parseFloat(seq.timebase) / TICKS, end = parseFloat(seq.end) / TICKS, spans = [];
for (var v = 0; v < seq.videoTracks.numTracks; v++) {
  var tr = seq.videoTracks[v];
  for (var i = 0; i < tr.clips.numItems; i++) {
    var c = tr.clips[i], at = 'V' + (v + 1) + ' ' + c.name + ' @' + c.start.seconds.toFixed(2);
    if (c.projectItem && c.projectItem.isOffline()) rep.push('HORS LIGNE ' + at);
    if (c.disabled) rep.push('DESACTIVE ' + at); else spans.push([c.start.seconds, c.end.seconds]);
  }
}
spans.sort(function (a, b) { return a[0] - b[0]; });
var cover = 0;
for (var s = 0; s < spans.length; s++) {
  if (spans[s][0] - cover > fr / 2) rep.push('TROU ' + cover.toFixed(2) + ' -> ' + spans[s][0].toFixed(2));
  cover = Math.max(cover, spans[s][1]);
}
if (end - cover > fr / 2) rep.push('TROU final ' + cover.toFixed(2) + ' -> ' + end.toFixed(2));
for (var a = 0; a < seq.audioTracks.numTracks; a++)
  rep.push('A' + (a + 1) + ' : ' + seq.audioTracks[a].clips.numItems + ' clips, ' + (seq.audioTracks[a].isMuted() ? 'MUETTE' : 'active'));
rep.join('\n');
