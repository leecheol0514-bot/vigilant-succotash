function calcDamage(level, power, atk, defn, stab, eff, crit, burn, extra) {
  const base = (((2 * level / 5 + 2) * power * atk / defn) / 50) + 2;
  const critMul = crit ? 1.5 : 1.0;
  const burnMul = burn ? 0.5 : 1.0;
  const rand = Math.random() * (1.0 - 0.85) + 0.85;
  const total = stab * eff * critMul * burnMul * rand * extra;
  let damage = Math.floor(base * total);
  if (damage < 1) {
    damage = 1;
  }
  return { damage, rand };
}

document.getElementById('damage-form').addEventListener('submit', function (event) {
  event.preventDefault();

  const level = Number(document.getElementById('level').value);
  const power = Number(document.getElementById('power').value);
  const atk = Number(document.getElementById('atk').value);
  const defn = Number(document.getElementById('def').value);
  const stab = document.getElementById('stab').checked ? 1.5 : 1.0;
  const eff = Number(document.getElementById('eff').value) || 1.0;
  const crit = document.getElementById('crit').checked;
  const burn = document.getElementById('burn').checked;
  const extra = Number(document.getElementById('extra').value) || 1.0;

  const result = calcDamage(level, power, atk, defn, stab, eff, crit, burn, extra);
  const text = `예상 피해량: ${result.damage}\n랜덤 계수: ${result.rand.toFixed(3)}\nSTAB: ${stab}\n상성: ${eff}\n크리티컬: ${crit ? '예' : '아니오'}\n화상: ${burn ? '예' : '아니오'}\n기타 보정: ${extra}`;
  document.getElementById('result').innerText = text;
});
