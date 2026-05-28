units = int(input("Enter the number of units used:"))
if units>=300:
    bill=units*8+500
    gst_amount=bill*0.18
    final_bill=bill+gst_amount
    print("Total bill is", bill)
    print("Bill with GST is", final_bill)
elif units>=0 and units<=50:
    print("You used less electricity so no bill")
elif units>=51 and units<=100:
    bill=units*5
    gst_amount=bill*0.18
    final_bill=bill+gst_amount
    print("Total bill is", bill)
    print("Bill with GST is", final_bill)
else: 
    bill=units*8
    gst_amount=bill*0.18
    final_bill=bill+gst_amount
    print("Total bill is", bill)
    print("Bill with GST is", final_bill)