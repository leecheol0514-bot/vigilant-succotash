import random

# 포켓몬 기술 피해 계산 프로그램입니다.
# 반복 실행이 가능하며 출력은 간결하고 정중한 표현으로 구성되어 있습니다.

def calc_damage(level, power, atk, defn, stab=1.0, eff=1.0, crit=False, burn=False, extra=1.0):
    # 기본 데미지 계산식
    base = (((2 * level / 5 + 2) * power * atk / defn) / 50) + 2

    # 크리티컬은 1.5배, 화상은 0.5배
    crit_mul = 1.5 if crit else 1.0
    burn_mul = 0.5 if burn else 1.0
    rand = random.uniform(0.85, 1.0)

    total = stab * eff * crit_mul * burn_mul * rand * extra
    damage = int(base * total)
    if damage < 1:
        damage = 1
    return damage


def ask_number(msg, default=None):
    while True:
        text = input(msg).strip()
        if text == "" and default is not None:
            return default
        try:
            return float(text)
        except ValueError:
            print("숫자만 입력해 주십시오.")


def ask_yes_no(msg):
    while True:
        text = input(msg).strip().lower()
        if text in {"y", "yes", "o", "ㅛ"}:
            return True
        if text in {"n", "no", "ㄴ"}:
            return False
        print("y 또는 n을 입력해 주십시오.")


def run_once():
    level = int(ask_number("포켓몬 레벨: "))
    power = int(ask_number("기술 위력: "))
    atk = ask_number("공격력 (물리면 Attack, 특수면 Sp. Attack): ")
    defn = ask_number("상대 방어력 (물리면 Defense, 특수면 Sp. Def): ")

    stab = 1.5 if ask_yes_no("기술 타입이 포켓몬 타입과 동일합니까? (y/n): ") else 1.0
    eff = ask_number("상성 효과 (2.0, 1.0, 0.5 등): ", default=1.0)
    crit = ask_yes_no("크리티컬이 발생합니까? (y/n): ")
    burn = ask_yes_no("화상 상태입니까? (y/n): ")
    extra = ask_number("기타 보정값 (없으면 엔터): ", default=1.0)

    dmg = calc_damage(level, power, atk, defn, stab=stab, eff=eff, crit=crit, burn=burn, extra=extra)

    print("\n=== 계산 결과 ===")
    print(f"예상 피해량: {dmg}")
    print("랜덤 계수가 적용되었습니다 (0.85~1.00).")


def main():
    print("포켓몬 기술 피해 계산기")

    while True:
        run_once()
        if not ask_yes_no("계속 실행하시겠습니까? (y/n): "):
            print("프로그램을 종료합니다.")
            break


if __name__ == "__main__":
    main()
