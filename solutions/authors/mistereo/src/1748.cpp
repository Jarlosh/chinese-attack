#include <iostream>
using namespace std;
void main () {
	__int64 min[] = {1L, 2L, 4L, 6L, 12L, 24L, 36L, 48L, 60L, 120L, 180L, 240L, 360L, 720L, 840L, 1260L, 1680L, 2520L, 5040L, 7560L, 10080L, 15120L, 20160L, 25200L, 27720L, 45360L, 50400L, 55440L, 83160L, 110880L, 166320L, 221760L, 277200L, 332640L, 498960L, 554400L, 665280L, 720720L, 1081080L, 1441440L, 2162160L, 2882880L, 3603600L, 4324320L, 6486480L, 7207200L, 8648640L, 10810800L, 14414400L, 17297280L, 21621600L, 32432400L, 36756720L, 43243200L, 61261200L, 73513440L, 110270160L, 122522400L, 147026880L, 183783600L, 245044800L, 294053760L, 367567200L, 551350800L, 698377680L, 735134400L, 1102701600L, 1396755360L, 2095133040L, 2205403200L, 2327925600L, 2793510720L, 3491888400L, 4655851200L, 5587021440L, 6983776800L, 10475665200L, 13967553600L, 20951330400L, 27935107200L, 41902660800L, 48886437600L, 64250746560L, 73329656400L, 80313433200L, 97772875200L, 128501493120L, 146659312800L, 160626866400L, 240940299600L, 293318625600L, 321253732800L, 481880599200L, 642507465600L, 963761198400L, 1124388064800L, 1606268664000L, 1686582097200L, 1927522396800L, 2248776129600L, 3212537328000L, 3373164194400L, 4497552259200L, 6746328388800L, 8995104518400L, 9316358251200L, 13492656777600L, 18632716502400L, 26985313555200L, 27949074753600L, 32607253879200L, 46581791256000L, 48910880818800L, 55898149507200L, 65214507758400L, 93163582512000L, 97821761637600L, 130429015516800L, 195643523275200L, 260858031033600L, 288807105787200L, 391287046550400L, 577614211574400L, 782574093100800L, 866421317361600L, 1010824870255200L, 1444035528936000L, 1516237305382800L, 1732842634723200L, 2021649740510400L, 2888071057872000L, 3032474610765600L, 4043299481020800L, 6064949221531200L, 8086598962041600L, 10108248702552000L, 12129898443062400L, 18194847664593600L, 20216497405104000L, 24259796886124800L, 30324746107656000L, 36389695329187200L, 48519593772249600L, 60649492215312000L, 72779390658374400L, 74801040398884800L, 106858629141264000L, 112201560598327200L, 149602080797769600L, 224403121196654400L, 299204161595539200L, 374005201994424000L, 448806242393308800L, 673209363589963200L, 748010403988848000L, 897612484786617600L, 1000000000000000001L};
	__int64 count[] = {1L, 2L, 3L, 4L, 6L, 8L, 9L, 10L, 12L, 16L, 18L, 20L, 24L, 30L, 32L, 36L, 40L, 48L, 60L, 64L, 72L, 80L, 84L, 90L, 96L, 100L, 108L, 120L, 128L, 144L, 160L, 168L, 180L, 192L, 200L, 216L, 224L, 240L, 256L, 288L, 320L, 336L, 360L, 384L, 400L, 432L, 448L, 480L, 504L, 512L, 576L, 600L, 640L, 672L, 720L, 768L, 800L, 864L, 896L, 960L, 1008L, 1024L, 1152L, 1200L, 1280L, 1344L, 1440L, 1536L, 1600L, 1680L, 1728L, 1792L, 1920L, 2016L, 2048L, 2304L, 2400L, 2688L, 2880L, 3072L, 3360L, 3456L, 3584L, 3600L, 3840L, 4032L, 4096L, 4320L, 4608L, 4800L, 5040L, 5376L, 5760L, 6144L, 6720L, 6912L, 7168L, 7200L, 7680L, 8064L, 8192L, 8640L, 9216L, 10080L, 10368L, 10752L, 11520L, 12288L, 12960L, 13440L, 13824L, 14336L, 14400L, 15360L, 16128L, 16384L, 17280L, 18432L, 20160L, 20736L, 21504L, 23040L, 24576L, 25920L, 26880L, 27648L, 28672L, 28800L, 30720L, 32256L, 32768L, 34560L, 36864L, 40320L, 41472L, 43008L, 46080L, 48384L, 49152L, 51840L, 53760L, 55296L, 57600L, 61440L, 62208L, 64512L, 65536L, 69120L, 73728L, 80640L, 82944L, 86016L, 92160L, 96768L, 98304L, 103680L};
	__int64 x;
	int n;
	cin >> n;
	for(int i=0; i<n; i++){
		cin >> x;
		int a=0;
		while(min[a]<=x)
			a++;
		cout << min[a-1] << " " << count[a-1] << endl;
	}
}