package org.velezreyes.quiz.question6;

public class VendingMachineImpl implements VendingMachine {

    private static VendingMachineImpl instance;

    private int insertedCents = 0;
    private int totalCents = 0;


    public static VendingMachine getInstance() {
        if (instance == null) {
            instance = new VendingMachineImpl();
        }
        return instance;
    }

    @Override
    public void insertQuarter() {
        this.insertedCents += 25;
    }

    @Override
    public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException {
        Drink drink = null;
        int price;
        String nameCurrentBeverage;
        boolean isBeverageFizzy;

        switch (name) {
            case "ScottCola":
                nameCurrentBeverage = name;
                isBeverageFizzy = true;
                price = 75;
                if (insertedCents >= price) {
                    insertedCents -= price;
                    totalCents += price;
                    drink = new Beverage(nameCurrentBeverage, isBeverageFizzy);
                } else {
                    throw new NotEnoughMoneyException();
                }
                break;

            case "KarenTea":
                nameCurrentBeverage = name;
                isBeverageFizzy = false;
                price = 100;

                if (insertedCents >= price) {
                    insertedCents -= price;
                    totalCents += price;
                    drink = new Beverage(nameCurrentBeverage, isBeverageFizzy);
                } else {
                    throw new NotEnoughMoneyException();
                }
                break;

            default:
                throw new UnknownDrinkException();

        }
        return drink;
    }

    ;
}

class Beverage implements Drink {

    private final String name;

    private final boolean fizzy;

    public Beverage(String name, Boolean fizzy) {
        this.name = name;
        this.fizzy = fizzy;
    }

    @Override
    public String getName() {
        return name;
    }

    @Override
    public boolean isFizzy() {
        return fizzy;
    }
}
